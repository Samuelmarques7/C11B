# 7. Por meio do dataset paises.csv, trace em uma mesmo plano cartesiano
# duas linhas com estilos customizados (marcador, cor e tipo de linhas
# diferentes) comparando o "GDP ($ per capita)" e o número de "Phones
# (per 1000)" dos países da Europa Ocidental (WESTERN EUROPE);

import pandas as pd
import matplotlib.pyplot as plt

dfPaises = pd.read_csv('paises.csv', delimiter=';')

dfEuropa = dfPaises[dfPaises['Region'].str.contains('WESTERN EUROPE')]

plt.xlabel('Países')
plt.ylabel('Valores')
plt.title('GDP (vermelho) x Phones (azul) - Europa Ocidental')

plt.plot(dfEuropa['Country'], dfEuropa['GDP ($ per capita)'], 'o-r',
         dfEuropa['Country'], dfEuropa['Phones (per 1000)'], 's--b')

plt.show()