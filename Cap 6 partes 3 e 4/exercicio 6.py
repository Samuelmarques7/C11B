# 6. Com o dataset paises.csv, trace um Boxplot comparando a distribuição do
# "GDP ($ per capita)" entre os países da América Latina e da Europa
# Ocidental, permitindo assim identificar mediana, dispersão e outliers de
# cada grupo;

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dfPaises = pd.read_csv('paises.csv', delimiter=';')

dfLatina = dfPaises[dfPaises['Region'].str.contains('LATIN AMER')]

dfEuropa = dfPaises[dfPaises['Region'].str.contains('WESTERN EUROPE')]

dfRegioes = pd.concat([dfLatina, dfEuropa], axis=0)

sns.boxplot(data=dfRegioes,
            x='Region',
            y='GDP ($ per capita)'
            )

plt.title("GDP: América Latina x Europa Ocidental")
plt.show()