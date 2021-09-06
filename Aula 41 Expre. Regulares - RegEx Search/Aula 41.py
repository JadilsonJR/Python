import re #RegEx

texto="Curso de Python do CFB cursos, canal do Youtube"

res=re.search("Pessoa", texto) # Retorna se o conteudo Foi encontrado ou não 
try:
    pi= res.start() #Posição Inicial 
    pf= res.end() #Posição Final 
    tam= pf-pi  # Tamanho da String

    print(res.start()) # Posição inicial da String
    print(res.end()) # Posicao Final da String 
    print(tam)

except:
    print("Não Encontrado ")