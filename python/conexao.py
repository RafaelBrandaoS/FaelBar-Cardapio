from mysql.connector import connect
from os import getenv
from dotenv import load_dotenv

load_dotenv()

DB_HOST = getenv('DB_HOST')
DB_USUARIO = getenv('DB_USUARIO')
DB_SENHA = getenv('DB_SENHA')
DB_BANCO = getenv('DB_BANCO')
DB_PORTA = getenv('DB_PORTA')

def criar_conexao():
    return connect(host=DB_HOST, user=DB_USUARIO, password=DB_SENHA, database=DB_BANCO, port=DB_PORTA)


def fechar_conexao(con):
    return con.close()
