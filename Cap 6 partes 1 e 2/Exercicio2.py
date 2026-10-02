import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

dfSpace = pd.read_csv('space.csv', delimiter=';')

# filtrando as missões de cada país
dfUSA = dfSpace[dfSpace['Location'].str.contains('USA')]
dfChina = dfSpace[dfSpace['Location'].str.contains('China')]

# retirando as empresas repetidas
empresasUSA = dfUSA['Company Name'].drop_duplicates()
empresasChina = dfChina['Company Name'].drop_duplicates()

# contando quantas empresas diferentes sobraram
qtUSA = len(empresasUSA)
qtChina = len(empresasChina)

plt.bar(['EUA', 'China'], [qtUSA, qtChina], color='green')
plt.show()