import cx_Oracle
#from cadastros.controller.cadastrosController import Cadastros

# Informações de conexão
username = ''
password = ''
host = ''  # Endereço do servidor
port = 1521        # Número da porta padrão do Oracle
service_name = ''  # Ou substitua por SID, caso esteja usando

# String de conexão
dsn = cx_Oracle.makedsn(host, port, service_name=service_name)

# Conectar ao banco de dados
connection = cx_Oracle.connect(username, password, dsn)

class Lojas:

    def __init__(self, lojas):
        
        self.lojas = lojas

    def listarLojas():

        lojas=[]
        # Criar um cursor
        cursor = connection.cursor()

        # Consulta SQL
        sql = f'SELECT nomedafilial FROM VW_FILIAL'

        # Executar a consulta
        cursor.execute(sql) 

        for nome in cursor:

            lojas.append(nome[0])         

        cursor.close()

        return lojas
