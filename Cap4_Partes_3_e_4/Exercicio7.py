# Quantas missões foram lançadas a partir de localizações que contêm "Russia " (coluna Location)?

import numpy as np

dataset = np.loadtxt('space.csv',delimiter=';',dtype=str,encoding='utf-8')

dataset = np.char.strip(dataset)

location = dataset[1:,2]

cond = np.char.find(location,'Russia') != -1

print(f"A quantidade de missoes lancadas a partir da Russia é : {np.sum(cond)}")