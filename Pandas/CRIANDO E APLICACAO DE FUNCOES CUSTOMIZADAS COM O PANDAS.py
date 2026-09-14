import pandas as pd

import numpy as np

#Funcao para dar 10% de desconto em alguma coisa

#Ciando uma função no python

ds = pd.read_csv('paises.csv', sep=';')

def tenPercent (x):
    return x * 0.9

#Buscando a coluna que guarda a taxa de natalidade de um pais

#print(ds.columns)

taxa_mortalidade = ds['Deathrate']

#print(taxa_mortalidade)

ds['Deathate -10%'] = taxa_mortalidade.apply(tenPercent)

print(ds.head(2))