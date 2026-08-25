#Conte e em seguida mostre quais são as diferentes Regiões do planeta segundo
#segundo este dataset


import numpy as np


dataset = np.loadtxt('paises.csv', delimiter=';', dtype=str, encoding='utf-8')

dataset = np.char.strip(dataset) # retira os espaços

#print(dataset[0:,0:4])

Region= np.unique(dataset[1:, 1])

print(Region, len(Region))

#for dados in dataset[1:]:
