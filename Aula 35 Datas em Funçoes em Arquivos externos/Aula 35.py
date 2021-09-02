import datetime

data=datetime.datetime.now()
nasc=datetime.datetime(2000, 10, 25)

print(data.day,"/",data.month,"/",data.year)
print(nasc.strftime("%A"))  #strftime configura as datas


# strftime() Opçoes
# %a Dia da Semana Resumido  EX: Quar
# %A Dia da Semana Completo Ex: Quarta-Feira
# %w Retorna o numero do Dia da Semana Ex: Domingo 0 
# %d Retorna o Dia do Mes 
# %b Nome do Mes Abreviado 
# %B Nome do Mes Completo
# %m Retorna o Numero do Mes
# %y Retorna o Ano com dois Digitos
# %Y Retorna o Ano com quatro digitos 
# %H Retorna Hora com dois digitos 00-23
# %I Retorna Hora 00-12
# %p AM / Pm 
# %M Retorna Minutos
# %s Retorna Segundos 
# %f Retorna Microsegundos 
# %j Retorna Dia do Ano Ex: 001 - 365
# %W Retorna o numero da Semana do Ano Ex: Semana 12