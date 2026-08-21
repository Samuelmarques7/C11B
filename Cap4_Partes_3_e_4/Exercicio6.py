# Qual a porcentagem de missões realizadas com foguetes cujo status
# é "StatusRetired " (coluna Status Rocket)?


import numpy as np


dataset = np.loadtxt('space.csv', delimiter=';', dtype=str, encoding='utf-8')

Status_Rocekt, quantidades = np.unique(dataset[1:, 5], return_counts=True)


for i in range(len(Status_Rocekt)):
    print(Status_Rocekt[i], quantidades[i])
    if Status_Rocekt[i] == 'StatusRetired':
        retired = quantidades[i]

porcentagem = (retired/(sum(quantidades)))*100

print(porcentagem)