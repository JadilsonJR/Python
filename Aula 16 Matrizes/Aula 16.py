carros=[["Modelo","HRV"],
        ["Fabricante","Honda"],
        ["Ano", 2016]] # Array / List ou Vetor Unidimencional 

print (carros[0][1])
# for x in carros:
#     print(x)

carros[2][1]= 2020   #Alterando um valor Da Lista Multidimensional  
carros.append(["Cor","Preto"])  #Adicionando um Valor 
        
for l,c in carros:
    print ("Linha: ", l, " | Coluna: ", str(c))