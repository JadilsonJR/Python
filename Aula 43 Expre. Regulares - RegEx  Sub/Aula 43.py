import re #RegEx

texto="Curso de Python do CFB cursos, canal do Youtube"

res=re.sub(" ","-", texto) # Ela substitui algo(espaço) por outra coisa(-) em uma string informada  
res=re.sub(",",".", res) #substituindo outra vez
print (res)

