import re #RegEx
pesq=input("Pesquisar: ")
texto="Curso de Python do CFB cursos, canal do Youtube"

res=re.findall(pesq, texto) #Procurar o que vc quer pesquisar dentro de algo

print(res) #imprime a colecao 

qtde=len(res) #Pegando a Quantidade numerica do que foi pesquisado
print("Quantidade: "+ str(qtde))

for x in res:
    print(x)
