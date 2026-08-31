# Questão 2
# Conte e em seguida mostre quais são as diferentes Regiões do planeta segundo
# este dataset;

import numpy as np

dataset = np.loadtxt('paises.csv',delimiter=';',dtype=str,encoding='utf-8')

dataset = np.char.strip(dataset)

region = dataset[1:,1]

regioes,quantidades = np.unique(region,return_counts=True)

print(f"Existem {np.size(regioes)} diferentes regioes no dataset")

for r , q in zip(regioes,quantidades):

    print(f"as regioes são: {r} e a quantidade é: {q}")
