# 6. Com base nos dados do dataset space.csv, trace um gráfico em torta
# ilustrando a porcentagem geral de foguetes com status "StatusActive" e
# "StatusRetired", considerando todas as empresas;

import pandas as pd
import matplotlib.pyplot as plt

dfSpace = pd.read_csv('space.csv', delimiter=';')

dfActive = dfSpace[dfSpace['Status Rocket'] == 'StatusActive']

dfRetired = dfSpace[dfSpace['Status Rocket'] == 'StatusRetired']

qtActive = len(dfActive)
qtRetired = len(dfRetired)

plt.pie(x=[qtActive, qtRetired],
        labels=['% StatusActive', '% StatusRetired'],
        autopct='%1.1f%%')
plt.show()