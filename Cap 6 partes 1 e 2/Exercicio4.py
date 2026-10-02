# 4. Utilizando o dataset space.csv, trace um gráfico em barras com as
# 5 empresas que mais tiveram missões com status “Failure”;

import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

dfSpace = pd.read_csv('space.csv', delimiter=';')

dfFailure = dfSpace[dfSpace['Status Mission'] == 'Failure']

falhasPorEmpresa = dfFailure.groupby('Company Name').count()['Status Mission']

# pegando as 5 empresas com mais falhas
top5 = falhasPorEmpresa.nlargest(5)

# traçando o gráfico em barras
plt.bar(top5.index, top5.values, color='blue')
plt.ylabel('Missões com falha')
plt.title('5 empresas com mais missões "Failure"')
plt.show()