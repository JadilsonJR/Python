import os

carros=[]

class Carro:
    nome=""
    potencia=0
    velMax=0
    ligado=False
    
    def __init__(self,nome,potencia):  #Metodo Construtor
        self.nome=nome
        self.potencia=potencia
        self.velMax=int(potencia)*2
        self.ligado=False

    def ligar(self):   #Metodo
        self.ligado=True

    def desligar(self):
        self.ligado=False

    def info(self):
        print("Nome.......: ",self.nome)
        print("Potencia...: ",str(self.potencia))
        print("Vel.Maxima.: ",str(self.velMax))
        print("Ligado.....: ", ("sim" if self.ligado else "Não"))

def Menu():  #Funçãonormal
    os.system("cls") or None
    print("1 - Novo Carro")
    print("2 - Informções Carro")
    print("3 - Excluir Carro")
    print("4 - Ligar Carro")
    print("5 - Desligar Carro")
    print("6 - Listar Carro")
    print("7 - Sair Carro")
    print("Quantidades de Carros",len(carros))
    
    opcao=input("Digite uma Opção: ")
    
    return int(opcao)

def NovoCarro():
    os.system("cls") or None   
    nome1=input("Nome do Carro: ")
    pot1=input("Potencia do Carro: ")
    car=Carro(nome1, pot1)
    carros.append(car)
    print("Novo Carro criado!")
    os.system("pause")

def informacao():
    os.system("cls")
    n=input("Informe o numero do carro que deseja informações: ") #Retorna uma string do numero
    try:  #Caso o Carro Exista
        carros[int(n)].info() #Pesquise o Carro na Lista e mostre suas informaçoes
    except: #Caso não exista o numero do Carro
        print("Carro não existe na Lista")
    os.system("pause")

def excluirCarro():
    os.system("cls")
    n=input("Informe o numero do carro que deseja deseja Excluir: ") #Retorna uma string do numero
    try:  #Caso o Carro Exista
        del carros[int(n)]  #Delete o carro na posição indicada 
    except: #Caso não exista o numero do Carro
        print("Carro não existe na Lista")
    os.system("pause")

def ligarCarro():
    os.system("cls")
    n=input("Informe o numero do carro que deseja ligar: ") #Retorna uma string do numero
    try:  #Caso o Carro Exista
        carros[int(n)].ligar()
    except: #Caso não exista o numero do Carro
        print("Carro não existe na Lista")
    os.system("pause")

def DesligarCarro():
    os.system("cls")
    n=input("Informe o numero do carro que deseja Desligar: ") #Retorna uma string do numero
    try:  #Caso o Carro Exista
        carros[int(n)].desligar() #Liga o Carro informado
    except: #Caso não exista o numero do Carro
        print("Carro não existe na Lista")
    os.system("pause")

def listarCarros():
    os.system("cls")
    posi=0
    for recebe in carros:
        print(posi, " - ", recebe.nome)
        posi+=1
    os.system("pause")    

retorno=Menu()


while (int(retorno)<7):
    if retorno == 1:
        NovoCarro()
    elif retorno == 2:
        informacao()
    elif retorno == 3:
        excluirCarro()
    elif retorno == 4:
        ligarCarro()
    elif retorno == 5:
        DesligarCarro()
    elif retorno == 6:
        listarCarros()
    retorno=Menu()

os.system("cls")

print("Programa Finalizado")
