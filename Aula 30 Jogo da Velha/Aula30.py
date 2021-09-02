import os
import random
from colorama import Fore, Back, Style

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
    print("Jogadas:", Fore.GREEN + str(jogadas) + Fore.RESET)



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

def verificarVitoria():
    global velha
    vitoria="n"
    simbolos=["X","O"]
    for s in simbolos:
        vitoria="n"
        #verificar linhas
        il=ic=0
        while il<3:
            soma=0
            ic=0
            while ic<3:
                if(velha[il][ic]==s):
                    soma+=1
                ic+=1
            if(soma==3):
                vitoria=s
                break
            il+=1
        if(vitoria!="n"):
            break

        #verificar Colunas
        il=ic=0
        while ic<3:
            soma=0
            il=0
            while il<3:
                if(velha[il][ic]==s):
                    soma+=1
                il+=1
            if(soma==3):
                vitoria=s
                break
            ic+=1
        if(vitoria!="n"):
            break
        #verifica diagonal 1 
        soma=0
        idiagonal=0
        while idiagonal<3:
            if(velha[idiagonal][idiagonal]==s):
                soma+=1
            idiagonal+=1
        if(soma==3):
            vitoria=s
            break
         #verifica diagonal 1 
        soma=0
        idiagonal_linha=0
        idiagonal_coluna=2
        while idiagonal_coluna>=0:
            if(velha[idiagonal_linha][idiagonal_coluna]==s):
                soma+=1
            idiagonal_linha+=1
            idiagonal_coluna-=1
        if(soma==3):
            vitoria=s
            break
    return vitoria

def redefinir():
    #Declarando Variaveis Globais 
    global velha
    global jogadas
    global quemJoga
    global maxJogadas
    global vit
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
while(jogarNovamente == "s"):
    while True:
        tela()
        JogadorJoga()
        PCJoga()
        tela()
        vit=verificarVitoria()
        
        if(vit!="n")or(jogadas>=maxJogadas):
            break

    print(Fore.RED + "Fim de Jogo" + Fore.YELLOW)
    if(vit == "X" or vit == "O"):
        print("Resultado: Jogador ", vit , " venceu")
    else:
        print("Resultado: Empate")

    jogarNovamente=input(Fore.BLUE +" Jogar Novamente ? [s/n]:"+ Fore.RESET)
    redefinir()