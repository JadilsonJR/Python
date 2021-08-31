#Dictionary Ordem CHAVE key / Valor value
carro={
    "Fabricante":"Honda",
    "Modelo":"HRV",
    "Ano":"2016",
    "Cor":"Prata"
}

fab= carro.get("Fabricante") #Pegando o Valor da Chave pelo metodo GET

cor=carro["Cor"]="Preto" #Alterando o Valor da Chave 

print(fab)
print(carro["Modelo"])  #Ao utilizar a chave ele mostra o Valor 
print(cor)

carro["Cambio"]="Automatico" #adicionando um novo valor

# for x in carro:
#     print(x) #imprime a Chave 
#     print(carro[x])  #Imprime o Valorr


for c,v in carro.items():  #Utilizando o metodo Itens em um Dicitionary conseguimos retornar as chaves e os valores
    print(c,":", v)

if "Modelo" in carro:    #Verificando se existe uma chave dentro do Dictionary
    print("Sim, Modelo é uma Chave")


carro.pop("Cambio") #del carro["Cambio"] Outra forma de remover


print ("Tamanho do Dicitonary", len(carro))   # TAmanho do Dictionary

carro.clear() #Limpa todo o Dictionary

print ("Tamanho do Dicitonary", len(carro)) 

################################################################################

Trasporte={         #Um dictionary com 3 chaves e cada chave cai ter mais um valor 
        "veiculos1":{
            "Fabricante":"Honda",
            "Modelo":"HRV"
        },

        "veiculos2": {
            "Fabricante":"Fiat",
            "Modelo":"Punto"
        },

        "veiculos3": {
            "Fabricante":"Ford",
            "Modelo":"Fusion"
        }

}

print(Trasporte["veiculos1"])
print(Trasporte["veiculos1"]["Fabricante"])

######################################################

veiculos1={
    "Fabricante":"Honda",
    "Modelo":"HRV"
}

veiculos2= {
    "Fabricante":"Fiat",
    "Modelo":"Punto"
}

veiculos3= {
    "Fabricante":"Ford",
    "Modelo":"Fusion"
}

Trasporte2={
    "C1":veiculos1,
    "C2":veiculos2,
    "C3":veiculos3, 
}

print (Trasporte2["C3"]["Fabricante"])



# Sobre o del e pop() é a seguinte:

# pop( ) = deleta provisoriamente o item, mas, se quiser pode chamá-lo de volta no comando print( )
# del = deleta permanentemente o item e não é possível chamá-lo de volta no comando print( )

# as vezes podemos usar a função pop( ) para mostrar qual foi o item deletado de uma lista / Dictionary