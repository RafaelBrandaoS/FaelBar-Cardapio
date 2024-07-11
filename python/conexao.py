import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_USUARIO = os.getenv('DB_USUARIO')
DB_SENHA = os.getenv('DB_SENHA')
DB_BANCO = os.getenv('DB_BANCO')
DB_PORTA = os.getenv('DB_PORTA')

def criar_conexao():
    return mysql.connector.connect(host=DB_HOST, user=DB_USUARIO, password=DB_SENHA, database=DB_BANCO, port=DB_PORTA)


def fechar_conexao(con):
    return con.close()
