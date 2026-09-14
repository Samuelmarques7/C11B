# CARREGANDO DATASETS COM PANDAS

from IPython.display import display

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

#print(ds[['Region','Climate','Service']])

#Calculando a porcentagem da polulação de cada pais do mundo
#Calculando a polulacao total do planeta
total_population = np.sum(ds['Population'])

print(f"Calculando a polulação total do planeta:{total_population}\n")


#Calculando a porcentagem de cada pais

seriesPorcPaises = (ds['Population']/total_population)*100

print(f"Calculando a porcentagem de cada pais:\n{seriesPorcPaises}\n")

#Adicionar esta series no dataset

ds['% Population'] = np.round(seriesPorcPaises,3)

#Criando uma v2 do Dataset com colluna nova

ds.to_csv('paises_v2.csv')

#Pegando os 5 paises que mais em gente

print(f"Pegando os 5 paises que mais tem gente:\n\n{ds.nlargest(5, '% Population')['Country']}\n")

#Pegando os 5 paises que menos tem gente

print(f"Pegando os 5 paises que menos tem gente:\n\n{ds.nsmallest(5, '% Population')['Country']}\n")


