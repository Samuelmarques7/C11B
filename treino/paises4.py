# Questão 4
# Conte quantos países são da América do Norte (NORTHERN AMERICA)
# segundo este dataset;

import numpy as np

dataset = np.loadtxt('paises.csv',delimiter=';',dtype=str,encoding='utf-8')

dataset = np.char.strip(dataset)

region = dataset[1:,1]

cond = np.char.find(region,'NORTHERN AMERICA') != -1

print(f"{np.sum(cond)} países são da América do Norte")