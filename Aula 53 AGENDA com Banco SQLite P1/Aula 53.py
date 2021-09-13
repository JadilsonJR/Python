import os 
import sqlite3
from sqlite3 import Error

##Criando Conexão 

def ConexaoBanco():
    caminho="E:\\Documents\\GitHub_Projetos\\Python\\Python\\Banco\\Agenda.db" #caminho ate o banco de dados
    conexao=None #Iniciando Variavel 
    try:   #Testando se houve a conexão 
        conexao=sqlite3.connect(caminho)  #Fazendo a conexão no SQLite com o caminho fornecido pela variavel 
    except Error as ex :  #Caso apareça algum erro exibi-lo
        print(ex)    
    return conexao # Tetornando a Conexão 

vcon=ConexaoBanco()  #Armazenando a conexao 

def menuPrincipal():  #Função para exibir as opçoes 
    os.system("cls")
    print("1 - Inserir Novo Registro: ")
    print("2 - Deletar Registro: ")
    print("3 - Atualizar Registro: ")
    print("4 - Consultar Registro por ID: ")
    print("5 - Consultar Registro por Nome: ")
    print("6 - Sair: ")

def menuInserir():
    print()

def menuDeletar():
    print()

def menuAtualizar():
    print()

def menuConsultarId():
    print()
    
def menuConsultarNomes():
    print()

opc=0 #Iniciando a Variavel do Loop 
while opc != 6:   #Definido Regra
    menuPrincipal()   #Chamando a função de escrita
    opc=int(input("Digite uma opção: ")) #Recebendo a opção do usuario e tratando a opção pois o inpult retorna tipo String
    if opc==1:
        menuInserir()
    elif opc==2:
        menuDeletar()
    elif opc==3:
        menuAtualizar()
    elif opc==4:
        menuConsultarId()
    elif opc==5:
        menuConsultarNomes()
    elif opc==6:
        #Sair
        os.system("cls")
        print("Programa Finalizado")
    else:
        #Caso seja uma opção não informada
        os.system("cls")
        print("Opção Invalida")
        os.system("Pause")
