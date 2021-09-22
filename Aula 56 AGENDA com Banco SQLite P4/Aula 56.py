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

def query(conexao,sql): #Função para realizar, Delete, Update e Insert 
    try: 
        c=conexao.cursor() #Criando a variavel para receber a conexão, com o metodo curso para executar a query
        c.execute(sql)  
        conexao.commit() # Realizando de Fato a alteração
    except Error as ex:
        print(ex) #Imprimindo o erro caso aconteça 
    finally:
        print("Operação Realizada com Sucesso")
       

    
def consultar(conexao,sql):
    c=conexao.cursor()
    c.execute(sql)  
    res= c.fetchall() #retorna os resultados das consultas 
    return res

def menuPrincipal():  #Função para exibir as opçoes 
    os.system("cls")
    print("1 - Inserir Novo Registro: ")
    print("2 - Deletar Registro: ")
    print("3 - Atualizar Registro: ")
    print("4 - Consultar Registros: ")
    print("5 - Consultar Registro por Nome: ")
    print("6 - Sair: ")

def menuInserir():
    os.system("cls")
    vnome=input("Digite o Nome: ")
    vtelefone=input("Digite o Telefone: ")
    vemail=input("Digite o E-mail: ")
    vsql="INSERT INTO tb_contatos (T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONTATO) VALUES ('"+vnome+"', '"+vtelefone+"', '"+vemail+"')"
    
    query(vcon, vsql)

def menuDeletar():
    os.system("cls")
    vid=input("Digite o ID do registro a ser deletado: ")
    vsql="DELETE FROM tb_contatos WHERE N_IDCONTATOS= "+vid 
    vcon=ConexaoBanco() 
    query(conexao, vsql)


def menuAtualizar():
    os.system("cls")
    vid=input("Digite o ID do registro a ser alterado: ")
    r=consultar(vcon, "SELECT * FROM tb_contatos WHERE N_IDCONTATOS="+vid)
    rnome=r[0][1]
    rtelefone=r[0][2]
    remail=r[0][3]

    vnome=input("Digite o Nome: ")
    vtelefone=input("Digite o Telefone: ")
    vemail=input("Digite o E-mail: ")

    if (len(vnome)==0):
        vnome=rnome
    if (len(vtelefone)==0):
        vtelefone=rtelefone
    if (len(vemail)==0):
        vemail=remail
    vsql="UPDATE tb_contatos SET T_NOMECONTATO='"+vnome+"', T_TELEFONECONTATO='"+vtelefone+"', T_EMAILCONTATO='"+vemail+"' WHERE N_IDCONTATOS="+vid
    query(vcon, vsql)

def menuConsultar():
    vsql="SELECT * FROM tb_contatos"
    res=consultar(vcon, vsql)
    vlimite=10
    vcontador=0
    for r in res:
        print("ID:{0: <3} Nome:{1: <30} Telefone:{2: <14} E-mail:{3: <30}".format(r[0],r[1],r[2],r[3]))
        vcontador+=1
        if(vcontador>=vlimite):
            vcontador=0
            os.system("pause")
            os.system("cls")
    print("Fim da Lista")
    os.system("pause")
def menuConsultarNomes():
    vnome=input("Digite o Nome: ")
    vsql="SELECT * FROM tb_contatos WHERE T_NOMECONTATO LIKE '%"+vnome+"%' "
    res=consultar(vcon, vsql)
    vlimite=10
    vcontador=0
    for r in res:
        print("ID:{0: <3} Nome:{1: <30} Telefone:{2: <14} E-mail:{3: <30}".format(r[0],r[1],r[2],r[3]))
        vcontador+=1
        if(vcontador>=vlimite):
            vcontador=0
            os.system("pause")
            os.system("cls")
    print("Fim da Lista")
    os.system("pause")

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
        menuConsultar()
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
vcon.close()
os.system("pause")