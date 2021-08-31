curso=" Curso de Python"  #Uma String é como se fosse um Array com um conjunto de Caracteres 

print(curso[10])#Selecionando um Letra utilizando um indice
print(curso[0:6]) #Delimitando uma Faixa de Intervalo 

print(curso.strip()) #retira os espaços vazios
print(curso.lower()) #converte para minusculo. 
print(curso.lower().strip()) #Podemos Unir os Metodos ou seja utilizar mais de um
print(curso.upper()) #converte para minusculo
print(curso.replace("Python","C")) #Substitui uma palavra por Outra selecionada 
a=(curso.split(" ")) #Ele quebra a string no indicador que vc selecionar neste exemplo um espaço ele irar armazenar na variavel e ele retorna o valor em FORMA DE LISTA 
print(a[1])
print("Tamanho:",len(curso)) #o Metodo len() retorna o tamanaho da String
