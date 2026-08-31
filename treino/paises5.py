# Questão 5
# Encontre qual país da América do Sul e Caribe (LATIN AMER. & CARIB)
# possui a maior renda per capita (GDP ($ per capita));

import numpy as np

dataset = np.loadtxt('paises.csv',delimiter=';',dtype=str,encoding='utf-8')

dataset = np.char.strip(dataset)

region = dataset[1:,1]

cond = np.char.find(region,'LATIN AMER. & CARIB') != -1

renda = dataset[1:,8].astype(float)

paises = dataset[1:,0]

idx = np.argmax(renda[cond])

print(idx)

print(f"O país que possui maior renda per capita é o {paises[cond][idx]}")