import funcoes      # Importa o arquivo com as funções
cpfs_validos = []  # Lista para armazenas os CPFs considerados válidos

# Captura a escolha do usuário
opcao = input("O que deseja fazer?\n1 - Gerar CPF(s) válidos\n2 - Verificar se um CPF é válido\n\n")

# Verifica qual a opção escolhida e executa a ação correspondente
if opcao=='1':
  for i in range(0, 500):
    cpf = funcoes.generate_valid_cpf()
    if funcoes.is_valid_cpf(cpf):
      cpfs_validos.append(cpf)
      with open("cpfs_validos.txt", 'a') as arquivo:
        arquivo.write(f"{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}\n")
  print(f"\nForam gerados {len(cpfs_validos)} CPFs válidos.\nResultados:")
  print(cpfs_validos)

elif opcao=='2':
  cpf = input("Digite o CPF que deseja testar (somente números): ")
  if funcoes.is_valid_cpf(cpf):
    print(f"O CPF {cpf} é válido!")
  else:
    print(f"O CPF {cpf} é inválido!")

else:
  print("Opção inválida!")