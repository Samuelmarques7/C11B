# 4. Utilizando do dataset mpg, analise a relação entre a potência dos
# veículos (horsepower) e o consumo de combustível (mpg), construindo uma
# visualização que permita identificar a tendência entre essas variáveis e
# interpretar seu comportamento;

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ds_mpg = sns.load_dataset('mpg')

sns.regplot(data=ds_mpg,
            x='horsepower',
            y='mpg',
            line_kws={'color': 'red'}
            )

plt.title("Relação entre potência e consumo")
plt.show()