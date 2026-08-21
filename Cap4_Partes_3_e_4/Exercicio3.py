# 3. Encontre quantas missões espaciais neste Dataset foram realizadas
# pelos Estados Unidos (EUA)

import numpy as np

dataset = np.loadtxt('space.csv',delimiter=';',dtype=str,encoding='utf-8')

print(dataset[0])

Eua = 0

for dados in dataset[1:]:
    if np.char.find(dados[2],'USA') != -1 :
        Eua += 1

print(Eua)