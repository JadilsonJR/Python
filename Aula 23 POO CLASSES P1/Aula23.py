#Classe é um conjunto de Regra de um determinado Objeto 
#Classe podemos considerar como uma planta de uma casa 
#objeto seria a casa instanciada ou seja iniciada
#Instaciar é igual a criar
#Criando uma classe
class carro:
    velMax= 0
    ligado=False
    cor=""

#Criando Objeto
c1=carro()
c2=carro()
c3=carro()
#instanciando o Objeto
c1.velMax=200
c1.cor="Preto"
c1.ligado=False

estado="Ligado" if c1.ligado else "Desligado"

print("Velocidade Maxima",c1.velMax)
print("Estado",estado)
print("Cor:",c1.cor)
