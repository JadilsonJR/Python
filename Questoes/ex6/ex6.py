# A música é feita de sons, que são ondas sonoras que vibram em uma frequência. As notas musicais principais são dó, ré, mi, fá sol, lá, si, representadas por (C, D, E, F, G, A, B) nesta ordem.

# A escala musical com estas sete notas principais e é subdividida em 12 notas com a distância entre duas notas consecutivas igual a 1/2 tom ou 1 semitom, pois entre Mi e Fá e Sí e Dó, não há sustenido/bemol (#, b). Desta forma a escala de semitons pode ser representada das seguintes formas:

# Crescente
# [C, C#, D, D#, E, F, F#, G, G#, A, A#, B]

# Decrescente
# [C, Db, D, Eb, E, F, Gb, G, Ab, A, Bb, B]





def gera_frequencia_nota(semitons):
    import math
    num=semitons
   
    def frequencia():
        if num>=0: #Verifica se é positivo
            if(num == 0):#caso o parametro seja 0 ele incrementa a divisao em 1 
                x=1
            x=num
            freq=440     
            valor_not_cres = freq*2**(x/12)
            def verifica(v):
                n = int(v)
                m = v 
                if m == n:
                    return str(int(m))
                else:
                    return str(round(valor_not_cres,4))
                return verifica(res)
            res_fre=verifica(valor_not_cres) 
            return res_fre          
        else:
            x=num
            freq=440
            valor_not_neg= freq*2**(x/12)
            def verifica(v):
                n = int(v)
                m = v 
                if m == n:
                    return str(int(m))
                else:
                    return str(f'{round(valor_not_neg,4):.4f}')
                return verifica(res)
            res_fre=verifica(valor_not_neg) 
            return res_fre          
        
    def letras(x):
        opc=x
        if(opc>0):
            notas_c=["A", "A#", "B","C", "C#", "D","D#", "E", "F", "F#", "G", "G#"]
            l=12
            if(opc<=11):
                res= opc
                return notas_c[res]
            elif(opc>=12 and opc <=23):
                res= opc-l
                return notas_c[res]
            elif(opc>=24 and opc <=35):
                res=(opc-(l*2))
                notas_c[res]
                return notas_c[res]
            elif(opc>=36 and opc <=47):
                res=(opc-(l*3))
                notas_c[res]
                return notas_c[res]
            elif(opc>=48 and opc <=59):
                res=(opc-(l*4))
                notas_c[res]
                return notas_c[res]
            elif(opc>=60 and opc <=71):
                res=(opc-(l*5))
                notas_c[res]
                return notas_c[res]
            elif(opc>=72 and opc <=74):
                res=(opc-(l*6))
                notas_c[res]
                return notas_c[res]
        else:
            res_neg=opc*-1
            l=12
            notas_d=["A", "Ab", "G","Gb", "F", "E", "Eb", "D", "Db", "C", "B","Bb"]
            if(res_neg<=11):
                res= res_neg
                return notas_d[res]

            elif(res_neg>=12 and res_neg <=23):
                res= res_neg-l
                return notas_d[res]

            elif(res_neg>=24 and res_neg <=35):
                res=(res_neg-(l*2))
                notas_d[res]
                return notas_d[res]

            elif(res_neg>=36 and res_neg <=47):
                res=(opc-(l*3))
                notas_d[res]
                return notas_d[res]

            elif(res_neg>=48 and res_neg <=59):
                res=(res_neg-(l*4))
                notas_c[res]
                return notas_d[res]

            elif(res_neg>=60 and res_neg <=71):
                res=(res_neg-(l*5))
                notas_d[res]
                return notas_d[res]

            elif(res_neg>=72 and res_neg <=74):
                res=(res_neg-(l*6))
                notas_d[res]
                return notas_d[res]

    res_frequencia= frequencia()
    res_letra= letras(num)
    return res_frequencia, res_letra
pass


print(gera_frequencia_nota(-6))