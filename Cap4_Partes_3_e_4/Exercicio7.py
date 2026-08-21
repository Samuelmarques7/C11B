# Quantas missões foram lançadas a partir de localizações que contêm "Russia " (coluna Location)?


import numpy as np

dataset = np.loadtxt('space.csv', delimiter=';', dtype=str, encoding='utf-8')

cond = np.char.find(dataset[1:, 2], 'Russia') != -1

print(np.sum(cond))