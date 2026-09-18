# 1. Crie duas Series com os seguintes valores:
# • seriesAno1: {‘Java’: 16.25, ‘C’: 16.04, ‘Python’: 9.85}
# • seriesAno2: {‘C’: 16.21, ‘Python’: 12.12, ‘Java’: 11.68}

import pandas as pd

import numpy as np

import math as mt

s1 = pd.Series ({'Java': 16.25, 'C': 16.04, 'Python': 9.85})
s2 = pd.Series({'C': 16.21, 'Python': 12.12, 'Java': 11.68})

# 2. Os valores das Series criadas na Questão 1 representam as fatias de
# mercado (porcentagem) de 3 linguagens de programação populares em
# dois anos consecutivos. Para cada ano, apresente a porcentagem total que
# elas juntas representam no mercado;

print (f"soma total que elas representam no mercado:{ sum(s1):.2f}%")

print (f"soma total que elas representam no mercado:{ sum(s2):.2f}%")

# 3. Apresente o crescimento/declínio no mercado de cada linguagem do
# primeiro ano para o segundo ano;

print(f"Crescimento/Declinio:\n{s2.subtract(s1)}")

# 4. Baseado nos resultados da Questão 3, mostre apenas os dados das
# linguagens que tiveram crescimento;

print(f"Linguagens que tiveram crescimento:\n{s2.subtract(s1)[s2.subtract(s1) > 0]}")

# 5. Se estas porcentagens de crescimento/declínio se mantivessem iguais
# para os próximos 2 anos, qual seria a linguagem mais popular?
# Dica: use o método nlargest(1) no final para retornar rapidamente a label
# CIÊNCIA DE DADOS COM PYTHON Prof. Renzo Paranaíba Mesquita
# e maior valor de uma Series.

taxa = s2.subtract(s1)

projecao2anos = s2 + (taxa*2)

mais_pupular = projecao2anos.nlargest(1)

print(mais_pupular)
