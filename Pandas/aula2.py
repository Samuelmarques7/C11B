# CARREGANDO DATASETS COM PANDAS

import pandas as pd

import numpy as np

ds = pd.read_csv('paises.csv', sep=';')

#print(ds)


#visualizando as colunas
#print(ds.columns)


#Extraidno registros do topo
#print(ds.head(5))

#Extraindo registros da base
#print(ds.tail(3))

print(ds[['Region','Climate','Service']])




