# Mostre o nome das empresas que já realizaram missões espaciais,
# juntamente com suas respectivas quantidades de missões (use
# o for no final para mostrar as informações)

import numpy as np


dataset = np.loadtxt('space.csv', delimiter=';', dtype=str, encoding='utf-8')

empresas, quantidades = np.unique(dataset[1:, 1], return_counts=True)

for i in range(len(empresas)):
    print(empresas[i], quantidades[i])

