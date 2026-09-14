import pandas as pd

import numpy as np

#SO FUNCIONA SE O DATASET TIVER AO MENOS UMA COLUNA DE DADOS CATEGORICOS

ds = pd.read_csv('paises.csv', sep=';')


#Contar o numero de paises por regiao


#Agrupando por região
group_region = ds.groupby('Region')

#print(group_region.count()['Country'])


#Somando a populacao de cada regiao


group_region = ds.groupby('Region')


print(f"Somando a população de cada região:\n{group_region.sum()['Population']}\n")



