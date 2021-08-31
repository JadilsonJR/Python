# l_carros = ["HRV", "Golf", "Polo", "Palio"] # Lista ou Array
# t_carros = ("HRV", "Golf", "Polo", "Palio") #Tupla se utiliza PARENTESES


# # for x in l_carros: 
# #     print(x)

# l_carros[0]="Uno"  # Na lista pode-se adicionar remover e substituir itens
# #t_carros[0]="Fox"  # Na Tupla não se pode substituir itens DIRETAMENTE,

# print(t_carros[0])

# print(t_carros[0])


t_carros = ("HRV", "Golf", "Polo", "Palio")
l_carros = list(t_carros)  # O list ta convertendo o TUPLA para LIST

l_carros[2]="Focus"  #Altero o Valor da Tupla que esta na LIST

t_carros=tuple(l_carros) # Adiciono o valor que estava na LIST para a TUPLA NOVAMENTE

print(t_carros[2])