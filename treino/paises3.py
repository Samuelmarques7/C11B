# Questão 3
# Mostre qual a taxa média de alfabetização (Literacy (%)) do planeta segundo
# este dataset;

import numpy as np

dataset = np.loadtxt('paises.csv',delimiter=';',dtype=str,encoding='utf-8')

dataset = np.char.strip(dataset)

literacy = dataset[1:,9].astype(float)

print(f"A a taxa media de alfabetização é: {literacy.mean():.2f}%")