from random import randint

# Verifica se todos os numeros do CPF são iguais
def all_equal(cpf):
  comparador = cpf[0]
  for digito in cpf:
    if(comparador != digito):
      return False
  return True

# Implementa o cálculo de validade de CPF
def is_valid_cpf(cpf):
  todos_iguais = all_equal(cpf)
  if(not todos_iguais):
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

# Gera um CPF aleatório
def generate_valid_cpf():
  cpf = randint(0, 99999999999)
  cpf = str(cpf)
  if(len(cpf)<11):
    complemento = '0'*(11-len(cpf))
    cpf = f"{complemento}{cpf}"
  return cpf