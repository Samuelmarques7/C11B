# 3. Encontre quantas missões espaciais neste Dataset foram realizadas
# pelos Estados Unidos (EUA)

import numpy as np

dataset = np.loadtxt('space.csv',delimiter=';',dtype=str,encoding='utf-8')

dataset = np.char.strip(dataset)

location = dataset[1:,2]

cond = np.char.find(location,'USA') !=-1

print(f"A quandide de missoes espaciais realizadas nos EUA é : {np.sum(cond)}")