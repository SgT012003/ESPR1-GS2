#----------------------------#
# Grupo do Projeto           #
#----------------------------#
# Diogo Julio       RM553837 #
# Victor Didoff     RM552965 #
# Vinicius Silva    RM553240 #
#----------------------------#------------------------------------------#
# Comando de Instalação para os imports                                 #
# pip install Flask requests pyserial mysql-connector-python Flask-Cors #
#-----------------------------------------------------------------------#

# Server Side
from flask import Flask, jsonify, request
from flask_cors import CORS

# Client Side
from datetime import datetime
import requests, uuid, os, json, serial

# Global Imports
import mysql.connector

# Server or Client Execution
server = True

# Client Configs
logfile = 'C:\\GlobalSolution\\datalog.json'
com_port = 'COM3'
baud_rate = 9600
guid = ''

# Global Configs
config = {
    'user': 'root',
    'password': '',
    'host': '127.0.0.1',
    'port': 3306,
    'database': 'global_solution'
}
# end

# Server Side Configs
app = Flask(__name__)
CORS(app)
# end

# extra commands for Client Side
def getLocation(): # from ip
    try:
        response = requests.get('https://ipinfo.io/')
        data = response.json()
        localizacao = data['loc'].split(',')
        latitude = localizacao[0]
        longitude = localizacao[1]
        return latitude, longitude
    except Exception as e:
        print(f"Erro ao obter localização: {e}")
        return None, None

def processData(data, uuid_name):
    latitude, longitude = getLocation()
    return {
    "GUID_coleta": f'{uuid.uuid1()}',
    "GUID_nome": f'{uuid_name}',
    "longitude": longitude,
    "latitude": latitude,
    "temperatura_ambiente": data[0],
    "temperatura_agua": data[1],
    "umidade": data[2],
    "turbidez": data[3],
    "impurezas": data[4],
    "data": f'{datetime.now().strftime("%d/%m/%Y %H:%M:%S")}'
}

def save_local(data):
    os.makedirs(os.path.dirname(logfile), exist_ok=True)
    try:
        if os.path.exists(logfile):
            with open(logfile, 'r') as file:
                local_data = json.load(file)
        else:
            local_data = []
        local_data.append(data)
        with open(logfile, 'w') as file:
            json.dump(local_data, file)
    except Exception as e:
        print(f"Erro ao salvar dados localmente: {e}")

def send_local_data():
    if not os.path.exists(logfile):
        return

    try:
        with open(logfile, 'r') as file:
            local_data = json.load(file)

        for data in local_data:
            columns = ', '.join(data.keys())
            values = ', '.join(f"'{value}'" if isinstance(value, str) else str(value) for value in data.values())
            command = f"INSERT INTO `global_solution`.`dados` ({columns}) VALUES ({values});"
            if querryMariaDB(command):
                local_data.remove(data)

        with open(logfile, 'w') as file:
            json.dump(local_data, file)

        if not local_data:
            os.remove(logfile)

    except Exception as e:
        print(f"Erro ao enviar dados locais para o servidor: {e}")
# end

# extra commands for Server Side
def json4response(response):
    return {
        "GUID_nome": response[0],
        "GUID_coleta": response[1],
        "longitude": response[2],
        "latitude": response[3],
        "temperatura_ambiente": response[4],
        "temperatura_agua": response[5],
        "umidade": response[6],
        "turbidez": response[7],
        "impurezas": response[8],
        "data": response[9]
    }
# end

# Default querry command 
def querryMariaDB(sqlcommand:str):
    response:str = ''
    try:
        conexao = mysql.connector.connect(**config)
        cursor = conexao.cursor()
        cursor.execute(sqlcommand)
        if sqlcommand.__contains__('SELECT'):
            response = cursor.fetchall()
        if sqlcommand.__contains__('INSERT'):
            conexao.commit()
    except Exception:
        print('Erro ao conectar ao banco de dados')
        return False
    finally:
        cursor.close()
        conexao.close()
        return response
# end

# Server Side Execution
if server == True:
    @app.route('/', methods=['GET'])
    def webserver():
        page = request.args.get('page', default=0, type=int)
        limit = 25
        offset = page * limit
        name = request.args.get('name', default='', type=str)

        try:
            command:str = ''
            if name == '':
                command = f'SELECT * FROM `global_solution`.`dados` ORDER BY `data` DESC, `GUID_nome` ASC LIMIT {limit} OFFSET {offset};'
                response = querryMariaDB(command)
            else:
                command = f"SELECT GUID_nome FROM `global_solution`.`dispositivos` WHERE nome LIKE '%{name}%'"
                response = querryMariaDB(command)

                if not response:
                    return jsonify([])
                
                response = "', '".join([row[0] for row in response])
                command = f"SELECT * FROM `global_solution`.`dados` WHERE GUID_nome IN ('{response}') ORDER BY `data` DESC, `GUID_nome` ASC LIMIT {limit} OFFSET {offset};"
                response = querryMariaDB(command)

        except Exception as e:
            return jsonify({"error": str(e)}), 500
        
        aux = [json4response(linha) for linha in response]
        return jsonify(aux)

    if __name__ == '__main__':
        app.run(debug=True)
# end

# Client Side Execution
if not server:
    ser = serial.Serial(com_port, baud_rate, timeout=1)

    try:
        while True:
            data = ser.readline().decode('utf-8').strip()
            if data:
                data = processData(data.split(','), guid)
                save_local(data)
                send_local_data()

    except KeyboardInterrupt:
        print("Leitura interrompida pelo usuário")
    finally:
        ser.close()
