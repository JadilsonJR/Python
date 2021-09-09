import sqlite3
from sqlite3 import Error
import os

######## Criar Conexão
def ConexaoBanco():
    caminho="E:\\Documents\\GitHub_Projetos\\Python\\Python\\Banco\\Agenda.db"
    conexao=None
    try:
        conexao=sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return conexao

vcon=ConexaoBanco()


def inserir(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)

res=True
while res:
    nome=input("Digite o seu Nome: ")
    telefone=input("Digite o seu Telefone: ")
    email=input("Digite o seu E-mail: ")
    vsql="INSERT INTO tb_contatos (T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONTATO) VALUES('"+nome+"','"+telefone+"','"+email+"')"
    res=input("Deseja continuar Registrando: [S]")
    
    if res != "S":
        res=False
    else:
        res=True

inserir(vcon, vsql)