# 8. Crie um dicionário para armazenar os dados de um produto (nome, preço e
# quantidade em estoque). Peça ao usuário os dados de 3 produtos diferentes e
# guarde cada dicionário em uma lista. No final, percorra a lista e mostre, para
# cada produto, seu nome e o valor total em estoque (preço × quantidade).

lista = []

print("Digite os dados de 3 produtos abaixo")

for i in range(3):
    produto = {}
    produto['Nome'] = input("Digete o nome do produto: ")
    produto['Preço'] = float(input("Qual o preço: "))
    produto['Quant em estoque'] = int(input("Qual a quantidade dispoivel em estoque: "))
    lista.append(produto)

for produto in lista:
    print("Nome: ",produto['Nome']," valor total: R$",produto['Quant em estoque']*produto['Preço'])
