# nome= input("Digite seu nome:") entrada de dados
# print("Nome digitado:", nome)

import os  #importando uma biblioteca para limpar o terminal automatico ao iniciar o sistema
os.system('cls')  #Comando do Windosn para limpar a tela

num1=int(input("Digite o Primeiro Valor:"))  #O input sempre Retorna como String
num2=int(input("Digite o Segundo Valor :"))
res=num1+num2

print("A soma dos valores :", num1,"+", num2, "é :", res)

