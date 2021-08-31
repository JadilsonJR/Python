
# #regras do While (FOR) Inicialização de Variavel de Controle, teste logico , 
# # Comandos dentro do While, Incremento ou deCremento da Variavel 

# i=0
# while i<=9 :
#     print(i)
#     i+=1
#     if(i>=5):
#         break
# print("Fim do Loop \n")   
# ##############################################

# print("##############################################")
# carros=["HRV", "Civic", "Prisma","Cruze"]
# i=0
# tam=len(carros)

# while i<tam :
#     print(carros[i])
#     i+=1
    
# print("\n Fim do Loop Carros")    

# ###########################################

#Cria a Lista Veiculos Onde ficara armazenado o que foi digitado

Veiculos=[]
Veiculo=input("Digite os Nomes dos Carros: ")  # Recebe a escrita e Armazena em VEICULO
tam=len(Veiculos)   # Mostra o Tamanho da Lista

while Veiculo !="Fim" :     # Preeche a Lista e so para quando o Resultado for Fim
    Veiculos.append(Veiculo)
    Veiculo=input("Digite os Nomes dos Carros: ")

#Limpa a Tela
import os
os.system("cls")

#Mostra os Carros Armazenados em Veiculos
print("Os Veiculos Armazenados Foram: ")
for x in Veiculos:
    print(x)






