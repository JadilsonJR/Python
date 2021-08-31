#

#Classe Pai ou Super Classe ou Base
#Criando uma classe
class NPC: 
    def __init__(self,nome,time,forca,municao):  #Criando Um metodo Construtor
        self.nome=nome
        self.time=time
        self.forca=forca
        self.municao=municao
        self.vivo=True
        self.energia=100

    def info(self):         #Imprimindo os Valores do Objetos
        print("Nome: ", self.nome)
        print("Time: ", self.time)
        print("Forca: ", self.forca)
        print("Munição: ",self.municao)
        print("Vivo: ", ("Sim " if self.vivo else "Não"))
        print("Energia: ", self.energia)
        print("=====================================")

class Soldado (NPC):  #Classe filho herdado a classe pai  (NPC)
    def __init__(self, nome, time,):  #Construtor da classe filho sobrescrevem o construtuor da classe pai, então estamos passando para a classe pai nome,time
        self.forca=200  #Recriando metodos
        self.municao=200 #Recriando Metodos

        super().__init__(nome, time, self.forca, self.municao) #Invoca os metodos da classe pai 

        #O self quer disser que ele quer passar o seu proprio valor que esta armazenado em seu escopo

class Guarda(NPC):
     def __init__(self, nome, time,):  
        self.forca=100  
        self.municao=20 
        super().__init__(nome, time, self.forca, self.municao) 
        super().info()

class Elite(NPC):
     def __init__(self, nome, time,):  
        self.forca=400  
        self.municao=500 
        super().__init__(nome, time, self.forca, self.municao) 
        def inf(self):  #Criando uma Função para chamar a função INfo da classe pai
            super().info()

#Instanciou o Objeto da Classe
s1=Guarda("Olho Vivo ",1)
s2=Soldado("Bala na Agulha ",1)
s3=Elite("Bixo Doido ",1)
s4=Guarda("Atento ",2)
s5=Soldado("Bizonho ",2)
s6=Elite("Samu ",2)

s1.vivo=False

s1.info()
s2.info()
s3.info()
s4.info()
s5.info()
s6.info()