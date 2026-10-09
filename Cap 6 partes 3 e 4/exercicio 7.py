# 7. Utilizando o dataset paises.csv, trace um Regplot relacionando a taxa de
# alfabetização (Literacy (%)) com a mortalidade infantil (Infant mortality (per
# 1000 births)), customizando a cor da linha de regressão;

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


dfPaises = pd.read_csv('paises.csv', delimiter=';')

print(dfPaises.columns)
sns.regplot(data=dfPaises,

            x='Literacy (%)',
            y='Infant mortality (per 1000 births)',
            line_kws={'color': 'green'}
            )

plt.title("Alfabetização x Mortalidade infantil")
plt.show()
