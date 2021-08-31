#Iterators

carros=["HRV","Polo","Jetta","Cruze","Fusion"]


itCarros=iter(carros) #Trasformou a listar em um Iterator

print(next(itCarros))  #imprime o primeiro da Lista
print(next(itCarros)) #A cada vez que chama o Next ele passa a lista
print(next(itCarros))
print(next(itCarros))

print(next(itCarros)) #Ao chegar no fim do Iterator ele manda uma mensagem 

#Pode ser usado em while como o controle while

#Maneira tradicional
# i=0
# while i<5:
#     print(carros[i])
#     i+=1

#Utilizando o Iterators como o controlador do while
while itCarros:
    try: #Caso tudo certo 
        print(next(itCarros))
    except StopIteration: #caso deu erro de fim do interator 
        print("Fim da Lista") #Mensagem de termino da Lista
        break  
#for c in carros: # O for é bastante utilizando para percorre listas
#   print(c)