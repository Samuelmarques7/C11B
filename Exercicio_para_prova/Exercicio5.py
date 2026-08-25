#Encontre qual páis da América do Sul e Caribe(LATIN AMER &
# CARIB) possui a maior renda per capita(GDP($ per capita));

import numpy as np

dataset = np.loadtxt('paises.csv', delimiter=';', dtype=str, encoding='utf-8')

dataset = np.char.strip(dataset) # retira os espaços

