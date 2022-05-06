def valor(v):
  n = int(v)
  m = v * 10
  s = n * 10
  if m == s:
    return 1
  else:
    return 2 
while True:
  n = float(input('valor = '))
  r = valor(n)
  #Agora vc pode brincar
  if r == 1:
    print('Você digitou um numero INTEIRO se imbecil !')
  elif r == 2: # Ou vc pode usar [ELSE]
    print('Você digitou um numero DECIMAL seu aderbal !')   