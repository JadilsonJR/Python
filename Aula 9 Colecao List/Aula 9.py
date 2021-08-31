carros=["HRV", "GOLF","ARGO","FOX"] #Criando Lista
carros.append("Fusion") #Adicionando um Item na Lista
carros.append("Focus")
carros.append("Polo")

carros.remove("Polo") #Removendo um item da Lista
carros.pop() #Remove o Ultimo Item da Lista na maneira FIFO 
del carros[2] #removendo por indice

#carros.clear() Limpa toda a lista

carros2=list(carros)  #Copiando uma Lista para outra 

carros2=["Fusca","Brasilia","Opala"] #Substituiu os carros da lista 2 

carros3=carros+carros2 #Unindo A lista do Carros + Carros 2 em Carros 3 



print("Numeros de Carros na Lista: ", str(len(carros)))
print("Numeros de Carros na Lista: ", str(len(carros2)))
print("Numeros de Carros na Lista: ", str(len(carros3)))
#print(carros[-1]) imprimindo a Lista de forma Inversa