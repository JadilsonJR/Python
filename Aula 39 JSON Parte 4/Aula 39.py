import json
#Carregando um arquivo externo 
with open('E:/Documents/GitHub_Projetos/Python/Python/Aula 39 JSON Parte 4/jogador.json') as f:
    jogador=json.load(f)

#Imprimindo Itens especifico de um Dictionary dentro de um Dictinary 
for a in jogador["Aeronaves"]:
    print (a["tipo"], " - " ,a["habilidade"])
