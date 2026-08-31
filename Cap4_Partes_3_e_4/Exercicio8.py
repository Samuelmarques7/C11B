#8. Encontre a empresa e o valor da missão mais cara de todo o Dataset.

import numpy as np

dataset = np.loadtxt('space.csv',delimiter=';',dtype=str,encoding='utf-8')

dataset = np.char.strip(dataset)

company = dataset[1:,1]

cost = dataset[1:,6].astype(float)

idx = np.argmax(cost)

print(f"A missão mais cara de todo o Dataset foi da empresa {company[idx]}, com valor de {cost[idx]:.2f}")