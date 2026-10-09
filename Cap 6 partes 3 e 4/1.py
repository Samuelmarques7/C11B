# 1. Utilizando o dataset Iris do Seaborn, para os dados apenas da espécie
# 'setosa', avalie a correlação entre suas variáveis numéricas, apresentando
# os valores das correlações e permitindo identificar quais variáveis estão
# mais correlacionadas;

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ds_iris = sns.load_dataset('iris')

ds_setosa = ds_iris[ds_iris['species'] == 'setosa']

corr = ds_setosa[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].corr()

sns.heatmap(corr,
            annot=True,
            fmt='.2f'
            )

plt.title("Correlação das variáveis da espécie setosa")
plt.show()
