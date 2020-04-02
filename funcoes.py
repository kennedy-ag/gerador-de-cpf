from random import randint

def all_equal(cpf):
  comparador = cpf[0]
  for i in cpf:
    if(comparador != i):
      return False
  return True

def is_valid_cpf(cpf):
  a = all_equal(cpf)
  if(not a):
    c = 10
    soma = 0
    for i in range(0, 9):
      soma = soma + (int(cpf[i])*c)
      c = c-1
    resto = soma%11
    if(resto==0 or resto==1):
      j = 0
    elif(resto>1 and resto<11):
      j = 11-resto
    c = 11
    soma = 0
    for i in range(0, 10):
      soma = soma + (int(cpf[i])*c)
      c = c-1
    resto = soma%11
    if(resto==0 or resto==1):
      k = 0
    elif(resto>1 and resto<11):
      k = 11-resto
    if(j==int(cpf[9]) and k==int(cpf[10])):
      return True
    else:
      return False
  else:
    return False

def generate_valid_cpf():
  cpf = randint(0, 44444444444)
  cpf = str(cpf)
  if(len(cpf)<11):
    complement = '2'*(11-len(cpf))
    cpf = "{0}{1}".format(cpf, complement)
  return cpf