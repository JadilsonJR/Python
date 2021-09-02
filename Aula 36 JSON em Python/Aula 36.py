import json
#convertendo um Json em Dictionary 
# carros_json='{"marca":"honda","modelo":"HRV","Cor":"Prata"}'

# carros=json.loads(carros_json)

# imprime as Chaves
# for x in carros:
#     print(x)
# imprime os Valores
# for x in carros.values():
#     print(x)

# for k,v in carros.items():
#     print(k, " - ",v)

#Convertendo um Json em Dictionary

carros={
        "marca":"honda",
        "modelo":"HRV",
        "Cor":"Prata"
}

carros_json=json.dumps(carros)

print(carros_json)
