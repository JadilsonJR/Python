
# linhas = int(input("Tamanho da arvore? "))
# tamanho = int(linhas * 2 - 1)
# espacos = int((tamanho - 1) / 2)
# i = 1
 
# while i <= linhas:
#  	print (" " * (espacos - i + 1), "*" * (2 * i - 1))
#  	i = i + 1


# def retorna_guiche_ingresso(ingresso_numero):
#     num_ing=ingresso_numero
    
    
#     qtd=[]
#     num=[] 
#     i=0  
#     x=0
#     def valor(): 
#         while i <= 6:
#             if(i == 0): 
#                 qtd.append(0)
#             else:
#                 qtd.append(2 * i - 1)     
#             i+=1
    
#     def guinche():
#         while i <=6:
#             num.append(i)     
#             i+=1

#     def teste():(
#         ult=len(qtd)-1
#         if num_ing < soma and num_ing < (soma-qtd):
#             print("ok")
#         else: 
#             print("No")    

#     def mostrar():
#         while x<=6:
#             print (" Ghinche",num[x],"->", qtd[x])  
#             x+=1
#         soma=sum(qtd)
#         print(soma)



#     num_ing 

#     return
   
   
# print(retorna_guiche_ingresso(26))



#MELHOR VERSAO 
# def retorna_guiche_ingresso(ingresso_numero):
#     num_ing=ingresso_numero
#     qtd=[]
#     num=[] 
#     i=0  
#     while i <= 6:
#         if(i == 0): 
#             qtd.append(0)
#         else:
#             qtd.append(2 * i - 1)     
#         i+=1
    
#     i=0
#     while i <=6:
#         num.append(i)     
#         i+=1
    
#     x=0
#     while x<=6:
#         print (" Ghinche",num[x],"->", qtd[x])  
#         x+=1
#     soma=sum(qtd)
#     print(soma)

#     ult=len(qtd)-1
#     ok=sum(qtd)-qtd[ult]
#     if num_ing < soma and num_ing > (qtd[ult]):
#         print("Guinche",ult,ok)
#     else: 
#         print("No",ult)

#     num_ing 
#     return
   
   
# print(retorna_guiche_ingresso(26))




#Teste 
# def retorna_guiche_ingresso(ingresso_numero):
#     num_ing=ingresso_numero
#     qtd=[]
#     num=[] 
#     i=0
#     while True:
#         if(i == 0): 
#             qtd.append(0)
#         else:
#             qtd.append(2 * i - 1)     
            
#             if num_ing in qtd:
#                 print("OK")
#                 break
#                 False
#             i+=1
#         i+=1
#         print("Ola")
        
        
#     i=0
    # while True:
    #     num.append(i)     
    #     i+=1
    #     if num < num_ing:
    #         False
    # x=0
    # while True:
    #     print (" Ghinche",num[x],"->", qtd[x])  
    #     x+=1
    #     if num < num_ing:
    #         False

    # soma=sum(qtd)
    # print(soma)

    # ult=len(qtd)-1
    # ok=sum(qtd)-qtd[ult]
    # if num_ing < soma and num_ing > (qtd[ult]):
    #     print("Guinche",ult,ok)
    # else: 
    #     print("No",ult)



#     num_ing 

#     return
   
   
# print(retorna_guiche_ingresso(26))


def retorna_guiche_ingresso(ingresso_numero):
    num_ing=ingresso_numero
     
    #Verifica qual Guinche
   
    
    def teste(x):
        
        num_ing=ingresso_numero
        ingresso=[]
        guinche=[]
        cont=x
        i=0
        while i <=cont:
            guinche.append(i)     
            i+=1
        
        #preenche a lista de quat de ingressos por colun
        i=0  
        while i <= cont:
            if(i == 0): 
                ingresso.append(0)
            else:
                ingresso.append(2 * i - 1)     
            i+=1
        
    
        x=0
        while x<= cont:
            print (" Ghinche",guinche[x],"->", ingresso[x])  
            x+=1


        soma=sum(ingresso)
        print("SOMA:",soma)

        ultimo=len(ingresso)-1
        print("Ultimo Indice Linha:",ultimo)

        
        ulti_num=sum(ingresso)-ingresso[ultimo]
        print("Penul Num Coluna",ulti_num)
        
        pes=ingresso[ultimo]
        print("Valor da ultima Coluna ",pes)

        if num_ing <= soma and num_ing >= ulti_num:
            print("Guinche",ultimo,num_ing)
        elif num_ing < ulti_num: 
            print("Guinche2",ultimo,num_ing)
            print("não foi")


    teste(num_ing)
    return
   
   
print(retorna_guiche_ingresso(3))
