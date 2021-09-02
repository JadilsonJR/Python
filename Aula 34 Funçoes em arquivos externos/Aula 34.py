# import Aula as AL #Chamando a Funçao de outro arquivo e dando um ALIAS 
# Aula.nome() 

# print(Aula.jogador["nome"])


from Aula import jogador #importando somente o Jogado

print(jogador["nome"])


import Aula  
res=dir(Aula)  #retorna os itens dentro da Biblioteca Aula
print(res)