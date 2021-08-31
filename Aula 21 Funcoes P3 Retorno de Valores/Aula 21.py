
valores=[1,2,3,2]

def somar(num):
    r=0
    for n in num:
        r+=n
    return r  #Retorna um valor para quem fez a chamada da Função
    
def val_Lista(num):
    for v in num:
        print(v)   

val_Lista(valores)

print("Soma = ", somar(valores))