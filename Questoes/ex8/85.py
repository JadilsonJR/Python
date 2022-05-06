# valores = [1,2,3,4,5]
# soma = [(val_1 + val_2) for val_1 in valores for val_2 in valores]
# for val in soma:
#     print(val)


def retorna_guiche_ingresso(ingresso_numero):
    num_ing=ingresso_numero
    ingresso=[]
    guinche=[] 
    #Verifica qual Guinche

    def ingresso(i):
        while i <= 5:
            if(i == 0): 
                ingresso.append(0)
        else:
            ingresso.append(2 * i - 1)     
        i+=1


    i=0
    while True:
        guinche.append(i)
        ingresso(i)    
        i+=1
        False
    #preenche a lista de quat de ingressos por colun
    i=0  
    
    
   
    x=0
    while x<=5:
        print (" Ghinche",guinche[x],"->", ingresso[x])  
        x+=1


    soma=sum(ingresso)
    print("SOMA:",soma)

    ult=len(ingresso)-1
    print("Ultimo Indice:",ult)
    ulti_num=sum(ingresso)-ingresso[ult]
    
    
    pes=ingresso[ult]
    print("Valor do ultimo indice ",pes)
    
    if num_ing <= soma and num_ing > ulti_num:
        print("Guinche",ult,num_ing)
    else: 
        while num_ing < ulti_num:
            
            ult=len(ingresso)-i
            ok=sum(ingresso)-ingresso[ult]
            print(ok)
            if num_ing == ok:
                print("OK",ok)
                break
            i+=1
            
    
    return
   
   
print(retorna_guiche_ingresso(25))