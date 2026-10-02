# 5. Por meio do dataset paises.csv, trace um gráfico de dispersão
# relacionando a renda per capita (GDP ($ per capita)) com a taxa de
# alfabetização (Literacy (%)) dos países da América Latina. Além disso,
# faça com que o tamanho de cada ponto represente a população do país;

import pandas as pd
import matplotlib.pyplot as plt

dfPaises = pd.read_csv('paises.csv', delimiter=';')

# filtrando somente os países da América Latina
dfLatina = dfPaises[dfPaises['Region'].str.contains('LATIN AMER')]

plt.scatter(dfLatina['GDP ($ per capita)'], dfLatina['Literacy (%)'],
            s=dfLatina['Population']/100000)

plt.xlabel('GDP ($ per capita)')
plt.ylabel('Literacy (%)')
plt.title('Renda per capita x Alfabetização - América Latina')
plt.show()