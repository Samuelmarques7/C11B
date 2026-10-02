import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns


#lendo o dataset paises.csv

dfPaises = pd.read_csv('paises.csv', delimiter=';')

# filtrando somente os países da América do Norte
dfNA = dfPaises[dfPaises['Region'].str.contains('NORTHERN AMERICA')]

# duas linhas no mesmo plano: mortalidade (vermelha) e natalidade (azul tracejada)
plt.plot(dfNA['Country'], dfNA['Deathrate'], 'o-r',
         dfNA['Country'], dfNA['Birthrate'], 's--b')

plt.xlabel('Países')
plt.ylabel('Taxa (por 1000 habitantes)')
plt.title('Mortalidade x Natalidade - América do Norte')
plt.legend(['Deathrate', 'Birthrate'])
plt.show()