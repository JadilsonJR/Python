import re #RegEx

texto="Curso de Python do CFB cursos, canal do Youtube"

res=re.split(",", texto)  # Ele divide a coleção atravez de um item informado nesse caso onde tem , 
#/s simboliza o space

print (res)

