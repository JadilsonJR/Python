x=1 #Tipo inteiro
x="CFB curso" #Tipo STR string
x=0.5 #Tipo Float
x= False #Tipo Boleano

n1=5;n2=2;x=complex(n1,n2) #exemplo de numero comprexo 
n1=5;n2=2;x=complex(1j)

print(x.real)
print(x.imag)

print("Valor :", str(x))
print("Tipo", str(type(x)))


Ve=["Carro","Aviao","Navio","Trem",1,0.58,True] #Declarando um Array pode ter qualquer tipo de Valor e pode ser substituido
Ve[0]="F1"

print("Imprima o Vetor na posição:",Ve[0])


Tu=("Carro","Aviao","Navio","Trem",1,0.58,True) #Tupla um vetor que não pode ser alterado
print("Imprima o Vetor na posição:",Tu[0])

ran=range(0,100,1) #List é como se fosse um Array ele vai criar de 0 a 100 adicionando de um a 1 

x={             #Dicionario eu não entendi direito
    "canal":"CFB Cursos",
    "curso":"Curso de Python",
    "nome":"Junior"
}

print("Valor :", x["canal"])
print("Tipo", str(type(x)))

x={5,7,4,3,2,1,0.5,1,2} #set ele organiza de forma Crescente e não repete os Valores

print("Valor :", str(x))
print("Tipo", str(type(x)))

x=frozenset({5,7,4,3,2,1,0.5,1,2}) # Congela o Set não deixando altera-lo
print("Valor :", str(x))
print("Tipo", str(type(x)))

