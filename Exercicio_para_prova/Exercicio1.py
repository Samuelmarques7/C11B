

import numpy as np

dataset = np.loadtxt('paises.csv', delimiter=';', dtype=str, encoding='utf-8')

dataset = np.char.strip(dataset) # retira os espaços

print(dataset[0])