texto=" Curso de Python"  #Uma String é como se fosse um Array com um conjunto de Caracteres 
palavra= "python"
res=palavra.upper() in texto.upper() #O Operdor IN faz uma busca e retorna se o valor esta ou não na variavel c
#res=palavra.upper() not in texto.upper() #Perguntando se não estar
print(res)


curso=" Curso de Python"  #Uma String é como se fosse um Array com um conjunto de Caracteres 
canal= "CFB"

conca= curso+"Do canal" + canal #Para concatenar strings se utiliza o +

print(conca)



dia=15
mes="dezembro"
ano=2021
cid="Brasilia"

data="{} de {} de {} \n \"{}\"" #Montando a Variavel com o PlaceHolder 
print(data.format(dia,mes,ano, cid)) #Montando o Print pelo metodo FORMAT primeiro fazemos o PLACEHOLDER depois indicamos quais variaveis usar
#\' \" \n \r \t \b 

#print(dia+ "de" + mes + "de" + ano + cid)