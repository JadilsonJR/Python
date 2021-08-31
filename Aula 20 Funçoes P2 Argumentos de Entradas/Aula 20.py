 #Funçoes é chamado por Def
 

def somar (*n):  #Argumentos Arbitrarios Utrilizando quando vão ser passados varios Valorees
    r=0
    for num in n:
        r+=num
    print("A soma é igual a:", r)


def soma2 (n):  
    r=0
    for num in n:
        r+=num
    print("A soma é igual a:", r)    

def carros (c ="Golf"):
    print("Modelos:", c)

carros



def texto (*t):
    for x in t:
        print(x)



somar(5,1,1,1,1)   
val=[1,2,3,4,5]

soma2(val)
texto("CFB","Python", "PC", "Curso")
