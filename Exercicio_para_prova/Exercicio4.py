#Conte quantos paises são da América do Norte(Northern America)
#segundo este dataset;

import numpy as np

dataset = np.loadtxt('paises.csv', delimiter=';', dtype=str, encoding='utf-8')

dataset = np.char.strip(dataset) # retira os espaços

colum_region = dataset[1:,1]

cond = np.char.find(colum_region,'NORTHERN AMERICA') != -1

paises_NA = colum_region[cond]

print(paises_NA)

print(f"Há {len(paises_NA)} países americanos")  #len: conta quantos objtos tem
