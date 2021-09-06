import re

nome="texto.txt"
arquivo= open("E:\Documents\GitHub_Projetos\Python\Python\Aula 45 Operacao em arquivos P2/"+nome,"rt") # Abrindo ou Criando o Arquivo 

# print(arquivo.read())  Abrir o arquivo para ler, com  
# print(arquivo.readline()) Ler somente a primeira linha 

res=re.sub("\s", "-", arquivo.readline())  #substituindo os espacos por -  
arquivo.close() #Fechando o Arquivo 

arquivo= open("E:\Documents\GitHub_Projetos\Python\Python\Aula 45 Operacao em arquivos P2/"+nome,"wt") #Abrindo o Arquivo 

arquivo.write(res)
arquivo.close()

print(res)