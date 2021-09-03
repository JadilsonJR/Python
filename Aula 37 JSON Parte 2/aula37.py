import json 

# carros_dictionary={
#     "marca":"honda",
#     "modelo":"HRV",
#     "cor":"prata"
# }
#dicitionary  -> objeto json 

#carros_list=["honda","Volks","Ford","Fiat","Chefrolet"]
#list -> array json 

#carros_tupla=("honda","Volks","Ford","Fiat","Chefrolet")
#tupla -> array json 

#carros_j=json.dumps(carros_dictionary, indent=4, separators=(": "," ="), sort_keys=True)  #separators troca o separador informa o elemento que ira ser substituido 

#sort_keys Ordena os elementos por ordem alfabetica 


# {
#     "nome":"Junior",
#     "time":"Aviadores",
#     "vivo":"True",
#     "Energia":"100",
#     "Mochila":["pederneira","corda","linha","arame"],
#     "Aeronaves":[
#         {"tipo":"transporte","habilidade":80},
#         {"tipo":"ataque","habilidade":100},
#         {"tipo":"reconhecimento","habilidade":50}
#     ]
# }

jogador_j='{"nome":"Junior","time":"Aviadores","vivo":"True","Energia":"100","Mochila":["pederneira","corda","linha","arame"],"Aeronaves":[{"tipo":"transporte","habilidade":80},{"tipo":"ataque","habilidade":100},{"tipo":"reconhecimento","habilidade":50}]}'

jogador=json.loads(jogador_j)

print(jogador)