#----------------------------#
# Grupo do Projeto           #
#----------------------------#
# Diogo Julio       RM553837 #
# Victor Didoff     RM552965 #
# Vinicius Silva    RM553240 #
#----------------------------#--------------------------------#
# Comando de Instalação para os imports                       #
# pip install Flask requests pyserial mysql-connector-python  #
#-------------------------------------------------------------#

from datetime import datetime
import requests, uuid, os, json, serial
import mysql.connector

# Configurações do cliente
logfile = 'C:\\GlobalSolution\\datalog.json'
com_port = 'COM3'
baud_rate = 9600
guid = ''

# Configurações globais
config = {
    'user': 'root',
    'password': '',
    'host': '127.0.0.1',
    'port': 3306,
    'database': 'global_solution'
}

# Função para obter localização (a partir do IP)
def getLocation():
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

# Função para processar os dados
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

# Função para salvar dados localmente em um arquivo JSON
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

# Função para enviar dados locais para o servidor
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

# Função para executar consulta no MariaDB
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
    except Exception as e:
        print('Erro ao conectar ao banco de dados')
        return False
    finally:
        cursor.close()
        conexao.close()
    return response

# Execução do cliente
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
