nome="texto.txt"
arquivo= open("E:\Documents\GitHub_Projetos\Python\Python\Aula 44 Operacao em arquivos P1/"+nome,"at") # Abrindo ou Criando o Arquivo 
# R - read - Ler
# A - append - Adicionar ou Anexar
# W - Write - Escrever
# X - create - criar 
# T - Texto - modo padrão
# B - Binario 

txt=input("Digite um texto: ") # Escrita recebida pelo Usuario 

arquivo.write(txt+"\n") #escrevendo no Arquivo 

arquivo.close() #Fechando o Arquivo 