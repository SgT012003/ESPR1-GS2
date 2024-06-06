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

from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector

# Configurações globais
config = {
    'user': 'root',
    'password': '',
    'host': '127.0.0.1',
    'port': 3306,
    'database': 'global_solution'
}

# Configurações do servidor
app = Flask(__name__)

# Função para formatar resposta JSON
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
    except Exception:
        print('Erro ao conectar ao banco de dados')
        return False
    finally:
        cursor.close()
        conexao.close()
        return response

# Rota do servidor
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
