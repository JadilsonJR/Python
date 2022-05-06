
# linhas = int(input("Tamanho da arvore? "))
# tamanho = int(linhas * 2 - 1)
# espacos = int((tamanho - 1) / 2)
# i = 1
 
# while i <= linhas:
#  	print (" " * (espacos - i + 1), "*" * (2 * i - 1))
#  	i = i + 1


def retorna_guiche_ingresso(ingresso_numero):
    num_ing=ingresso_numero
    
    tamanho=(num_ing*2-1)
    espacos = int((tamanho - 1) / 2)
    i=1
    # range(num_ing)
    # vet=[]    
    # while i <= 10:
    #     print (" Ghinche",i,"->", (vet.append((2 * i - 1))))       
    #     i+=1

    while i <= 10:
        print (" Ghinche",i,"->", (i))       
        i+=1
    return
   
    # vet1=iter(vet)
    # while vet1:
    #     try: #Caso tudo certo 
    #         print(next(vet1))
    #     except: #caso deu erro de fim do interator 
    #         print("Fim da Lista") #Mensagem de termino da Lista
    #         break  
   
print(retorna_guiche_ingresso(26))