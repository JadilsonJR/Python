
class carro:
    velMax= 0
    ligado=False
    cor=""
    #Metodo Construtor inicia toda vez quando instancia a classe
    def __init__(self,vm,lig,cor):  #Self indica que ira passar o metodo para a propria classe
        self.velMax=vm
        self.ligado=lig
        self.cor=cor

    def mostrar(self):
        estado= "Ligado" if self.ligado else "Desligado"
        print("Velocidade Maxima: ",self.velMax)
        print("Estado: ",estado)
        print("Cor:",self.cor)

    def ligar(self):
        self.ligado=True

    def Desligado(self):
        self.ligado=False   

    def Andar(self):
        if(self.ligado):
            print("Carro Andando\n")
        else:
            print(("Carro Parado"))         

#Criando Objeto e passando os valores para o metodo contrutor


c1=carro(200, False, "Preto")
c2=carro(150, False, "Azul")
c3=carro(300, True, "Vermelho")

c1.ligar()
c1.Andar()
c1.mostrar()
c2.mostrar()
c3.mostrar()