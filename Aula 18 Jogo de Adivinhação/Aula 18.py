import random
import os


erros=0
sorteados=random.randrange(0,100)
jogador=int(input("Digite seu numero: "))

while(sorteados != jogador):
    os.system('cls')
    if(sorteados > jogador):
        print("ERRO, o numero sorteado é maior")
    elif(sorteados < jogador): 
        print("ERRO, o numero sorteado é Menor")
    erros+=1
    jogador=int(input("Digite seu numero: "))


print("Numero",jogador, "Voce acertou em:", erros+1,"tentativas" )