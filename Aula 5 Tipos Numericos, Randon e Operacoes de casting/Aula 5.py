import random #importando a biblioteca RAMDOM

num_i=10
num_f=1.5
num_complexo=1j


x=int(num_f) #Passando o valor para o X e convertendo para Inteiro
x=float(num_i) ##Passando o valor para o X e convertendo para Float

num_aleatorios=random.randrange(0,59) #Gerando um numero aleatorio de 0 a 59

x=num_aleatorios


#STR converte inteiro para string e o STR(type()) Converte Tipo para string
print("Valor:", str(x), " - ", "Tipo", str(type(x)) ) 

num_aleatorios=[random.randrange(0,59),random.randrange(0,59),random.randrange(0,59)]  #Gerando Valores Aleatorios e armazenando em uma LISTA ou ARRAY
x=num_aleatorios

print("Valor 1 :", str(x[0]) ) 
print("Valor 2 :", str(x[1]) ) 
print("Valor 3 :", str(x[2]) ) 