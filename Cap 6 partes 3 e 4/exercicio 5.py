import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 5. Utilizando o dataset paises.csv, calcule a correlação entre "GDP ($ per
# capita)", "Literacy (%)", "Infant mortality (per 1000 births)" e "Phones (per
# 1000)", apresentando o resultado em um Heatmap com os valores numéricos
# exibidos;
dfPaises = pd.read_csv('paises.csv', delimiter=';')
corr = dfPaises[['GDP ($ per capita)', 'Literacy (%)',
                 'Infant mortality (per 1000 births)', 'Phones (per 1000)']].corr()

sns.heatmap(corr,
            annot=True,
            fmt='.2f'
            )

plt.title("Correlação entre indicadores dos países")
plt.show()