# 4. Encontre qual foi
# a missão mais cara realizada pela empresas
# “SpaceX"

import numpy as np

dataset = np.loadtxt('space.csv',delimiter=';',dtype=str,encoding='utf-8')

dataset = np.char.strip(dataset)

company = dataset[1:,1]

cond = company == 'SpaceX'

cost = dataset[1:,6].astype(float)

detail = dataset[1:,4][cond]

idx = np.argmax(cost[cond])

print(f"A missao mais cara realizada pela empresa Spacex tem o valor de: {cost[cond][idx]} e os detalhes da missao é:{detail[idx]}")

