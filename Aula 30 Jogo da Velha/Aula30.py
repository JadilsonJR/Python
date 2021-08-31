import os
import random
 


#Declarando Variaveis Globais 

jogarNovamente="s"
jogadas=0
quemJoga=2  #2 é a pessoa 1 é o PC
maxJogadas=9
vit="n" #Para ver se Venceu 
velha=[
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def tela():
    global velha #Sempre que utilizar a variavel global declarar como "global"
    global jogadas
    os.system("cls")
    print("    0      1     2")
    print("0: ", velha[0][0], " | ", velha[0][1], " | ", velha[0][2])
    print("   ---------------")
    print("1: ", velha[1][0], " | ", velha[1][1], " | ", velha[1][2])
    print("   ---------------")
    print("2: ", velha[2][0], " | ", velha[2][1], " | ", velha[2][2])
    print("Jogadas:", jogadas)

tela()

def JogadorJoga():
    global jogadas
    global quemJoga
    global vit
    global maxJogadas

    if quemJoga==2 and jogadas <maxJogadas:
        try:
            l=int(input("Linha: "))
            c=int(input("Coluna: "))
            while velha[l][c] != " ":
                os.system("cls")
                tela()
                print("Espaço ocupado Digite outro!")
                l=int(input("Linha: "))
                c=int(input("Coluna: "))
            velha[l][c]="X"
            quemJoga=1
            jogadas+=1
        except:
            print("Linha e/ou Coluna invalida!")


def PCJoga():
    global jogadas
    global quemJoga
    global vit
    global maxJogadas

    if quemJoga==1 and jogadas <maxJogadas:
        l=random.randrange(0,3)
        c=random.randrange(0,3)
        while velha[l][c] != " ":
            l=random.randrange(0,3)
            c=random.randrange(0,3)
        velha[l][c]="O"
        quemJoga=2
        jogadas+=1

while True:
    tela()
    JogadorJoga()
    PCJoga()