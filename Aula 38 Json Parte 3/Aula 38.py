import json 

jogador_j='{"nome":"Junior","time":"Aviadores","vivo":"True","Energia":"100","Mochila":["pederneira","corda","linha","arame"],"Aeronaves":[{"tipo":"transporte","habilidade":80},{"tipo":"ataque","habilidade":100},{"tipo":"reconhecimento","habilidade":50}]}'

jogador=json.loads(jogador_j) #Carregando o Json para formarto string em Python 


#Mostrar as Chaves

# for c in jogador:
#     print(c)


#Mostrar os Itens (Conjunto chave e valor)

# for i in jogador.items():
#     print(i)

#Mostra os Valores
# for v in jogador.values():
#     print(v)

#valor Especifico 
# print(jogador["time"])


#Itens da Mochila (Lista dentro do Dictionary)

# for im in jogador["Mochila"]:
#     print(im)


#Imprimindo Dictionary dentro de um Dictinary 
# for a in jogador["Aeronaves"]:
#     print (a)

#Imprimindo Itens especifico de um Dictionary dentro de um Dictinary 
for a in jogador["Aeronaves"]:
    print (a["tipo"], " - " ,a["habilidade"])

