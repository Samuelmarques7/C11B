# 8. Por meio do dataset space.csv, usando o conceito de subplot(), trace
# dois gráficos de barras separados lado a lado: à esquerda, as 5 empresas
# com mais missões de sucesso; à direita, as 5 empresas com mais missões
# de falha.

import pandas as pd
import matplotlib.pyplot as plt

dfSpace = pd.read_csv('space.csv', delimiter=';')

dfSuccess = dfSpace[dfSpace['Status Mission'] == 'Success']
dfFailure = dfSpace[dfSpace['Status Mission'] == 'Failure']


sucessosPorEmpresa = dfSuccess.groupby('Company Name').count()['Status Mission']
falhasPorEmpresa = dfFailure.groupby('Company Name').count()['Status Mission']


top5Success = sucessosPorEmpresa.nlargest(5)
top5Failure = falhasPorEmpresa.nlargest(5)


plt.subplot(1, 2, 1)
plt.title('Top 5 - Missões de Sucesso')
plt.bar(top5Success.index, top5Success.values, color='green')


plt.subplot(1, 2, 2)
plt.title('Top 5 - Missões de Falha')
plt.bar(top5Failure.index, top5Failure.values, color='red')

plt.show()