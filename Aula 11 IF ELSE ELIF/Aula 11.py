
a= 10 
b= 5
op = "0"
if op == "+":
    res=a+b
    print("Operação Soma, o Resultado foi de:", a ,"+", b ,"=" , res )

elif op == "-":     # O ELSE no Python é o elif 
    res=a-b
    print("Operação Subtração, o Resultado foi de:", a ,"-", b ,"=" , res )

elif op == "/":
    res=a/b
    print("Operação Subtração, o Resultado de:", a ,"/", b ,"=" , res )
    
elif op == "*":
    res=a*b
    print("Operação Subtração, o Resultado de:" , a ,"*", b ,"=" , res )
else:     #O else funciona como o DEFAULT do SWITCH
    print("Operacao invalida")

clima="sol"
lugar=""
dinheiro=450

if clima == "sol" and (dinheiro > 300 and dinheiro <500):
    lugar="clube"
else:
    lugar="cinema"

print("Vou ao :", lugar)