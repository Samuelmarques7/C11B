#8. Encontre a empresa e o valor da missão mais cara de todo o Dataset.

import numpy as np


dataset = np.loadtxt('space.csv', delimiter=';', dtype=str, encoding='utf-8')

print(dataset[0])

empresa, cost = dataset[1:, 1], dataset[1:, 6]

maior = 0

for i in range(len(empresa)):
    if float(cost[i]) > maior:
        maior = float(cost[i])
        big = empresa[i]

print(big, maior)

