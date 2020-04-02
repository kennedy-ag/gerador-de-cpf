import funcoes
cpfs_validos = []
for i in range(0, 100):
  cpf = funcoes.generate_valid_cpf()
  if(funcoes.is_valid_cpf(cpf)):
    print("CPF válido!")
    cpfs_validos.append(cpf)
    a = open("cpfs_validos.txt", 'a')
    a.write("{0}{1}{2}{1}{3}{4}{5}{6}".format(cpf[0:3], '.', cpf[3:6], cpf[6:9], '-', cpf[9:11], "\n"))
    a.close()
  else:
    print("CPF inválido!")
print()
print("Terminado com sucesso!\nResultados:")
if(len(cpfs_validos)!=0):
  print(cpfs_validos)
else:
  print("Nada para mostrar!")