# O objetivo desta atividade é criar um programa simples em Python para gerenciar um cadastro de compras e vendas de produtos.

# Crie um menu interativo que permita ao usuário escolher entre as seguintes opções:

# 1Registrar uma compra.

# 2Registrar uma venda.

# 3Verificar o saldo total das vendas.

# 0Sair do programa.

# Crie duas listas, uma para armazenar as compras e outra para armazenar as vendas. Cada registro nas listas deve conter informações como o nome do produto, a quantidade e o valor unitário.

# Ao registrar uma compra, solicite ao usuário que insira o nome do produto, a quantidade e o valor unitário. Adicione essas informações à lista de compras.

# Ao registrar uma venda, solicite ao usuário que insira o nome do produto, a quantidade e o valor unitário. Adicione essas informações à lista de vendas.

# Ao verificar o saldo total das vendas, calcule o lucro total subtraindo o valor total das compras do valor total das vendas. Exiba o lucro na tela.

# Certifique-se de que o programa possa lidar com erros, como entradas inválidas ou divisão por zero. Também atente-se a indentação ao enviar o código pelo sistema.

produtosComprados = False
produtosVendidos = False
while True:

  print("\n")
  print("1 - Registrar uma compra")
  print("2 - Registrar uma venda")
  print("3 - Verificar o saldo total das vendas")
  print("0 - Sair do programa")
  print("\n")
  
  opcao = int(input("Digite a opção desejada: "))


  if(opcao == 1):
    nomeProduto1_compra = input("1 - Digite o nome do produto comprado:")
    quantidadeProduto1_compra = int(input("Digite a quantidade comprada:"))
    valorProduto1_compra = float(input("Digite o valor unitario:"))

    print("\n")
    print("Produto adicionado: " + nomeProduto1_compra)
    print(f"Quantidade: {quantidadeProduto1_compra}")
    print(f"Valor unitario: {valorProduto1_compra}")
    print("\n")

    nomeProduto2_compra = input("2 - Digite o nome do produto comprado:")
    quantidadeProduto2_compra = int(input("Digite a quantidade comprada:"))
    valorProduto2_compra = float(input("Digite o valor unitario:"))

    print("\n")
    print("Produto adicionado: " + nomeProduto2_compra)
    print(f"Quantidade: {quantidadeProduto2_compra}")
    print(f"Valor unitario: {valorProduto2_compra}")
    print("\n")

    nomeProduto3_compra = input("3 - Digite o nome do produto comprado:")
    quantidadeProduto3_compra = int(input("Digite a quantidade comprada:"))
    valorProduto3_compra = float(input("Digite o valor unitario:"))

    print("\n")
    print("Produto adicionado: " + nomeProduto3_compra)
    print(f"Quantidade: {quantidadeProduto3_compra}")
    print(f"Valor unitario: {valorProduto3_compra}")
    print("\n")

    produtosComprados = True


  if(opcao == 2):
    if(produtosComprados == True):
      nomeProduto1_venda = input("1 - Digite o nome do produto vendido:")
      quantidadeProduto1_venda = int(input("Digite a quantidade vendida:"))
      valorProduto1_venda = float(input("Digite o valor unitario:"))

      print("\n")
      print("Produto vendido11: " + nomeProduto1_venda)
      print(f"Quantidade: {quantidadeProduto1_venda}")
      print(f"Valor unitario: {valorProduto1_venda}")
      print("\n")

      nomeProduto2_venda = input("2 - Digite o nome do produto vendido:")
      quantidadeProduto2_venda = int(input("Digite a quantidade vendida:"))
      valorProduto2_venda = float(input("Digite o valor unitario:"))

      print("\n")
      print("Produto vendido11: " + nomeProduto2_venda)
      print(f"Quantidade: {quantidadeProduto2_venda}")
      print(f"Valor unitario: {valorProduto2_venda}")
      print("\n")

      nomeProduto3_venda = input("3 - Digite o nome do produto vendido:")
      quantidadeProduto3_venda = int(input("Digite a quantidade vendida:"))
      valorProduto3_venda = float(input("Digite o valor unitario:"))

      print("\n")
      print("Produto vendido11: " + nomeProduto3_venda)
      print(f"Quantidade: {quantidadeProduto3_venda}")
      print(f"Valor unitario: {valorProduto3_venda}")
      print("\n")

      produtosVendidos = True

    else:
      print("\n")
      print('Voce tem que comprar os produtos antes de vendelos!')    

  if(opcao == 3):

    print("\n")
    print('error')    

    if(produtosComprados == True and produtosVendidos == True):

      valorTotal_compras = (quantidadeProduto1_compra * valorProduto1_compra) + (quantidadeProduto2_compra * valorProduto2_compra) + (quantidadeProduto3_compra * valorProduto3_compra)
      valorTotal_vendas = (quantidadeProduto1_venda * valorProduto1_venda) + (quantidadeProduto2_venda * valorProduto2_venda) + (quantidadeProduto3_venda * valorProduto3_venda)
      lucro =  valorTotal_compras - valorTotal_vendas

      print("\n")
      print(f"Saldo total das vendas: {valorTotal_vendas}")
      print(f"O lucro foi de: {lucro}")

    else:
      print("\n")
      print('Voce tem que vender os produtos!')  

  if(opcao == 0):
    break