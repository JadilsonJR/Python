def calculadistanciabandapercorre(numerorodadaensaios,numeroshows):
    num_ens = numerorodadaensaios
    num_show= numeroshows
    i=0
    x=0
    rodada=0
    p=0
    while i != num_ens:
        rodada= rodada + (140*250)
        i+=1
    while x != num_show:
        p= p + (42*250)
        x+=1
    res=rodada+p
    return res
    pass 

print(calculadistanciabandapercorre(2,0))


# 6 amigos (Ana, Bia, Cadu, Duda, Edu e Fabi) tem uma banda de rock, moram próximos ao centro da cidade. O mapa é o que está aqui abaixo, mostrando onde cada um mora.

# Eles sempre revezam os ensaios cada dia na casa de um integrante e costumam tocar em um pub no lugar P.

# Crie uma função que calcule a soma da quantidade de quilômetros são percorridos no total pelos participantes, permitindo que seja informado a quantidade de rodadas de ensaios e shows que a banda fez.

# Suponha a distância das laterais dos quarteirões são de 250m e desconsidere a largura das ruas.