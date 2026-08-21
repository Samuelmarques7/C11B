# 4. Faça um programa que leia o nome e peso de 3 pessoas e no final mostre o
# nome da pessoa mais pesada e a mais leve;

lista = []

for i in range(3):
    dados = {}
    dados['Nome'] = input("Digite o seu nome: ")
    dados['Peso'] = int(input("Qual o seu peso? "))
    lista.append(dados)


pesada = max(lista, key=lambda dados: dados['Peso'])
leve = min(lista, key=lambda dados: dados['Peso'])

print(pesada)
print(leve)