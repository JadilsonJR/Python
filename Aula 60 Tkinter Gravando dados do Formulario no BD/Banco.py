import sqlite3
from sqlite3 import Error 
import os

pastaAPP=os.path.dirname(__file__)#retorna o nome do Diretorio
nomeBanco=pastaAPP+"\\agenda.db"

def ConexaoBanco():
    con=None
    try:
        con=sqlite3.connect(nomeBanco) #Iniciando conexão
    except Error as ex: #caso algum erro
        print(ex)   #Mostrar o Erro
    return con

def DQL(query): #Função Select
    vcon=ConexaoBanco()  #Recebe o retorno da conexão a cada chamada
    c=vcon.cursor() 
    c.execute(query) 
    res=c.fetchall() #Retorna todos os resultados do select
    return res

def DML(query): #Insert, Delet, Update
    try:
        vcon=ConexaoBanco()  #Recebe o retorno da conexão a cada chamada
        c=vcon.cursor() 
        c.execute(query)
        vcon.commit() #Efetuar a mudança
        vcon.close()
    except Error as ex: #caso algum erro ocorra
        print(ex)   #Mostrar o Erro
    return con