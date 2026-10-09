# 2. Utilizando do dataset titanic, proponha um gráfico que apresente a
# distribuição das idades dos passageiros, diferenciando os dados por sexo e
# incluindo uma curva de densidade (KDE);

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ds_titanic = sns.load_dataset('titanic')

sns.histplot(data=ds_titanic,
             x='age',
             hue='sex',
             kde=True)
plt.title("Distribuição das idades por sexo")
plt.show()