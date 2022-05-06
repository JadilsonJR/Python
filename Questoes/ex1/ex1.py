# Uma banda vai se apresentar numa arena onde, do palco até a última pessoa que está assistindo ao show, tem uma distância d (d pode ter diversos valores: 0,35 km, 0,6 km, 1,02 km).

# Sabendo que a velocidade do som é 340 m/s, crie uma função que retorne em aproximadamente quanto tempo, em milisegundos, o som sai da caixa de som até ser ouvido pela última pessoa?

import math

def retorna_tempo_arena_em_milisegundos(distancia,velocidade):
    dist=float(distancia)*1000
    vel=velocidade
    tempo = (dist / vel)
    tempo2=(round(tempo*1000,2))
    
    res=round(tempo2-int(tempo2),2)

    if(res>0.5):
        tempo = math.ceil(tempo2)
        print("Maior que 0.5 ", tempo)
    else:
        tempo = math.floor(tempo2)
        print("Menor que 0.5 ", tempo)

    return tempo 

print(retorna_tempo_arena_em_milisegundos("0.45",340))


# import math

# def retorna_tempo_arena_em_milisegundos(distancia,velocidade):
#     dist=float(distancia)*1000
#     vel=velocidade
#     tempo = (dist / vel)
#     tempo_mili=math.ceil((tempo*1000))
#     pass 
#     return tempo_mili
    