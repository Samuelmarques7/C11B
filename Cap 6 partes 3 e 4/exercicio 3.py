# 3. Utilizando novamente o dataset titanic, analise a distribuição das idades
# dos passageiros em função da classe, segmentando os dados por sexo, de
# modo a construir uma visualização que permita comparar a tendência
# central, a dispersão e possíveis valores extremos entre os grupos;

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ds_titanic = sns.load_dataset('titanic')

sns.boxplot(data=ds_titanic,
            x='class',
            y='age',
            hue='sex'
            )
plt.title("Idades por classe e sexo")
plt.show()
