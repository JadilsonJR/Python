# Um show organizado, com pessoas verificando ingressos, e os seguranças olhando os participantes foi feito com o público de p pessoas (suponha que pode ser, por exemplo, 2.749). Para as pessoas entrarem, a média de tempo entre entregar o ingresso e poder acessar a área dos shows é de s segundos (suponha, por exemplo, 50).

# Para agilizar a entrada, a produção do evento disponibilizou n portões de entrada (suponha 8). Qual o tempo mínimo, em minutos, para que todos os participantes entrem completamente na área dos shows?




import math
def retorna_tempo_minimo_em_minutos(p,s,n):
# Fazendo a regra de 3 simples para descobrir pessoas por minutos
    p_minuto=60/s
    passa_por_m = p_minuto*n
#Realizando a regra de 3 composta 
    x2=passa_por_m
    x3=p/x2+1
#Formatando resultado
    res=round(int(x3))

    resultado=math.ceil(res)

    pass

    return print(resultado)

retorna_tempo_minimo_em_minutos(2749,50,8)