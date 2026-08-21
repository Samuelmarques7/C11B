# 4. Encontre qual foi
# a missão mais cara realizada pela empresas
# “SpaceX
# ”
import numpy as np


dataset = np.loadtxt('space.csv', delimiter=';', dtype=str, encoding='utf-8')

print(dataset[0])

cond = dataset[1:, 1] == 'SpaceX'

missoes_spacex = dataset[1:][cond]

maior = 0

for dados in missoes_spacex:
    if float(dados[6]) > maior:
        maior = float(dados[6])

print(maior)