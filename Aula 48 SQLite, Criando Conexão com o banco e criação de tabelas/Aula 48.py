import sqlite3
from sqlite3 import Error

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

####### Criar Tabela

vsql="""CREATE TABLE tb_contatos(
            N_IDCONTATOS INTEGER PRIMARY KEY AUTOINCREMENT,
            T_NOMECONTATO VARCHAR (30),
            T_TELEFONECONTATO VARCHAR (14),
            T_EMAILCONTATO VARCHAR (30) 
        );"""


######Rodar o comando 

def criarTabela(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        print("Tabela Criada")
    except Error as ex:
        print(ex)


criarTabela(vcon, vsql)
vcon.close()