# Faça um slicing no dataset para mostrar apenas o País (Country), Região
# (Region), População (Population) e Area (Area (sq. mi.)) dos países contidos
# nele;

import numpy as np

dataset = np.loadtxt('paises.csv',delimiter=';',dtype=str,encoding='utf-8')

dataset = np.char.strip(dataset)

print(dataset[0:,0:4])