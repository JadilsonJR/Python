#Funçoes Lamda são funçoes simples e anonimas ou seja não prescisa colocar o nome da função  

#a lambda inicia com LAMBDA

    #Criou a função e passou dois argumentos e associou o que ela tem que fazer 
soma=lambda a,b:a+b
print(soma(2,5))

mult=lambda a,b,c,:(a+b)* c
print(mult(2,5,3))

#Forma direta sem armazena-la 
print((lambda a,b:a-b)(3,2))

#Passando uma função na Lambda 

r1=lambda x,func:x+func(x)  #Inicia a lambda de baixo 

res=r1(2, lambda x:x*x)  
    # o dois vai parar no x
print(res)
res=r1(2, lambda x:x+3)  
    
print(res)