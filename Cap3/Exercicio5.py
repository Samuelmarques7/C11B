# 5. Desenvolva um programa que leia o nome, idade e sexo de n pessoas. No
# final, mostre:
# a-A média de idade do grupo;
# b-Quantas mulheres têm menos de 20 anos.
# Dica: em Python, os operadores booleanos básicos são and, or e not


lista = []

n = int(input("Digite o numero de pessoas: "))

for i in range(n):
    dados = {}
    dados['Nome'] = input("Digite o seu nome: ")
    dados['Idade'] = int(input("Qual a sua idade? "))
    dados['Sexo'] = input("Qual o sexo? ")
    lista.append(dados)

soma = 0

for pessoa in lista:
    soma += pessoa['Idade']

media = soma/len(lista)

print("A media de idade do grupo é -> ", media)

quant = 0

for pessoa in lista:
    if pessoa['Sexo'] == 'F' and pessoa['Idade'] < 20:
        quant = quant + 1