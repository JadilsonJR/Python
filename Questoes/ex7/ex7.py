# Um festival de rock é formado de um palco único, e a área do show (que é um círculo) é dividida em 8 setores de áreas iguais. A área total do show possui aproximadamente Areamaior m2, sendo que a parte central (ala VIP) tem Areamenor m2.

# Será preciso fazer uma busca na ala popular no setor 3, para encontrar a baqueta que o baterista da banda The XPTOs jogou para o público, mas era a baqueta preferida dele e ele acabou jogando por engano, mas antes, é preciso saber qual o tamanho da área de busca!

# Você consegue ajudar o pessoal fazendo uma função que calcule a área de busca de acordo com o tamanho informado da área do show e o tamanho da área VIP?


def tamanho_setor_busca(areamaior,areamenor):
    Ar_ma=areamaior
    Ar_me=areamenor

    Descontar_Area=(Ar_ma - Ar_me)
    res=Descontar_Area/8

    def verifica(v):
        n = int(v)
        m = v 
        if m == n:
            return (int(m))#retorn 1
        else:
            return  float(m)#retorn 2  
    
    return (verifica(res))
pass 

print(tamanho_setor_busca(2834,314))




# def tamanho_setor_busca(areamaior,areamenor):
#     Ar_ma=areamaior
#     Ar_me=areamenor

#     Descontar_Area=(Ar_ma - Ar_me)
#     res=Descontar_Area/8
#     return str(int(res))
# pass