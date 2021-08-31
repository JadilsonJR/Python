#Serve para fazer um tratamento de erro, informando se ha erros

x=10  # Para não da erro e não cair no execept
#Rotina Completa do Tratamento try,execept, else, finally

try :
    print(x)

except NameError:  #executa se o try encontra um erro, NameErro é o erro quando a variavel não exite
    print("Erro")  #indica o que caso haja o erro
    print ("Variavel não Definida")

except :
    print("Erro não definido")

else:
    print("Tudo Certo")

finally: #executa de qualquer forma com ou sem erro
    print("Fim do Programa")


num=3
if num <1:
    raise Exception("Valor não Permitido") #criando uma exesseção, delimitando um erro caso aquilo aconteça
num = "s"
if not type(num) is int:
    raise Exception("Somente Numero Inteiros")
else:
    print(num)    