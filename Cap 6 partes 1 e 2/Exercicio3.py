# 3. Por meio do dataset space.csv, trace um gráfico em torta
# ilustrando a porcentagem de missões da empresa Roscosmos que
# deram certo e que deram errado;
import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

dfSpace = pd.read_csv('space.csv', delimiter=';')

Roscosmos = dfSpace[dfSpace['Company Name'].str.contains('Roscosmos')]

# filtrando as missões que deram certo e contando
Success = Roscosmos[Roscosmos['Status Mission'] == 'Success']
qtSuccess = len(Success)

# o restante são as que deram errado
qtFailure = len(Roscosmos) - qtSuccess

# traçando o gráfico em torta

autopct='%1.1f%%'
plt.pie(x=[qtSuccess, qtFailure],
        labels=['% Missões que deram certo', '% Missões que deram errado'],
        autopct=autopct)
plt.show()