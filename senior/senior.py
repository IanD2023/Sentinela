import cx_Oracle
from cadastros.controller.cadastrosController import Cadastros
import os

# Informações de conexão
username = ''
password = ''
host = ''  # Endereço do servidor
port = 1521        # Número da porta padrão do Oracle
service_name = ''  # Ou substitua por SID, caso esteja usando

# username=os.environ['username']
# password=os.environ['password']

# String de conexão
dsn = cx_Oracle.makedsn(host, port, service_name=service_name)

# Conectar ao banco de dados
connection = cx_Oracle.connect(username, password, dsn)

class ConsultarMatricula:

    def __init__(self, nome, matricula, ativo, codigodafilial, nomedosetor, cpf):
        self.nome = nome
        self.matricula = matricula
        self.ativo = ativo
        self.codigodafilial = codigodafilial
        self.nomedosetor = nomedosetor.replace("-"," ")
        self.cpf = cpf

    def Consultar(matricula):
        # Criar um cursor
        cursor = connection.cursor()

        # Consulta SQL
        sql = f'SELECT nome, matricula, ativo, codigodafilial, nomedosetor, cpf FROM vw_colaborador WHERE matricula = {matricula}'

        # Executar a consulta
        cursor.execute(sql)

        if (cursor):
        
            # Recuperar os resultados
            for nome, matricula, ativo, codigodafilial, nomedosetor, cpf in cursor:
                ##print(f'Nome: {nome}, Matricula: {matricula},cpf: {cpf}, Situação {ativo} Codfilial: {codigodafilial}, Setor: {nomedosetor} ')
                cursor.close()
                return ConsultarMatricula(nome.strip(), matricula, ativo, codigodafilial, nomedosetor, cpf)


        sql = f'''SELECT B.NOMFUN, B.NUMCAD, B.SITAFA, A.NOMEDOSETOR, B.NUMCPF
                  FROM MIDDLEWARE.VW_SETOR A, SENIOR.R034FUN B
                  WHERE B.NUMLOC = A.CODIGO AND B.NUMCAD = {matricula}'''

        cursor.execute(sql)  

        for nome, matriculaColab, ativo, nomedosetor,cpf in cursor:
                
                if ativo == '7': ativo = 'false'
                else: ativo = 'true'

                cursor.close()
                print(nome.strip(), matriculaColab, ativo, '1', nomedosetor, cpf)

                return ConsultarMatricula(nome.strip(), matriculaColab, ativo, '1', nomedosetor, cpf)  

                ##nome, matricula, ativo, codigodafilial, nomedosetor, cpf           



    def ConsultarMatricula(matricula):

        cadastro=Cadastros().buscaMatricula(matricula)

        return cadastro
