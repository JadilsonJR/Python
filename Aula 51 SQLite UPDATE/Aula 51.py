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

#Inserir 
def inserir(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)


# nome=input("Digite o seu Nome: ")
# telefone=input("Digite o seu Telefone: ")
# email=input("Digite o seu E-mail: ")
# vsql="INSERT INTO tb_contatos (T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONTATO) VALUES('"+nome+"','"+telefone+"','"+email+"')"
# res=input("Deseja continuar Registrando: [S]")


#inserir(vcon, vsql)


#Deletar 
def deletar(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()

    except Error as ex:
        print(ex)

    finally:
         print("Registro Removido ")

#vsql="DELETE FROM tb_contatos WHERE N_IDCONTATOS = 3"

#deletar(vcon, vsql)


#Update

def atualizar(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()

    except Error as ex:
        print(ex)

    finally:
         print("Registro Atualizado ")

vsql="UPDATE tb_contatos SET T_NOMECONTATO='Bruno', T_TELEFONECONTATO='(12) 4567-8999', T_EMAILCONTATO='bruno@gmail.com' WHERE N_IDCONTATOS = 1"

atualizar(vcon, vsql)