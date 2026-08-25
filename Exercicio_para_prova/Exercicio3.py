# Mostre qual a taxa média de alfabetização(literacy(%))
# do planeta segundo este dataset

import numpy as np


dataset = np.loadtxt('paises.csv', delimiter=';', dtype=str, encoding='utf-8')

dataset = np.char.strip(dataset) # retira os espaços


colum_alfa = dataset[1:,9].astype(float)

media = np.mean(colum_alfa)

print(media)
