# Baseado nos commandos que vimos até
# o momento e no Datasetfornecido, crie scripts em Python que respondam às seguintes
# perguntas:
# 2. Qual a media de gastos de uma missão especial se baseando em
# missões que possuam valores disponíveis (>0)?

import numpy as np

dataset = np.loadtxt('space.csv',delimiter=';',dtype=str,encoding='utf-8')

dataset = np.char.strip(dataset)

cost = dataset[1:,6].astype(float)

cond = cost > 0

media = cost[cond].mean()

print(f"A média de gastos de uma missão é: {media:.2f}")

# A media é dada pela soma das missoes dividido pela quantidade total de missoes