def calculadistanciabandapercorre(numerorodadaensaios,numeroshows):
    
    num_ens = numerorodadaensaios
    num_show= numeroshows
    i=0
    x=0
    rodada=0
    p=0
    cont=0
    while cont<num_ens:
        while i <= num_ens:
         rodada= rodada + (163.8*250)
         i+=1 
         cont+=1
    print(rodada)
     
    cont=0
    while cont<num_show:
        while x <= num_show:
         p+=18.2*250
         x+=1
         cont+=1
    
    res=rodada+p
    
    return res

    # n_amigos=[1,2,3,4,5,6]
    # i=0 
    # if( i == n_amigos[i]):
    #     qtd_lados_tot=14
    #     dis_perc = dist*qtd_lados_tot


print(calculadistanciabandapercorre(2,1))