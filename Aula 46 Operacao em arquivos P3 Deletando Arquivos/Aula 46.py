import re
import os 
nome="texto.txt"
caminho=open("E:/Documents/GitHub_Projetos/Python/Python/Aula 46 Operacao em arquivos P3 Deletando Arquivos/") 
if os.path.exists(caminho+nome):
    print("Arquivo Existente")
else:    
    f=open(caminho+nome,"x")
    f.close()

if os.path.exists(caminho+nome):
    os.remove(caminho+nome)
else:
    print("Arquivo Inexistente")


# f.close()
# os.remove(caminho+nome)