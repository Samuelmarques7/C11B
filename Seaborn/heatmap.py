
import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns


#importando o dataset tips

ds_tips = sns.load_dataset('tips')

#selecionando as colunas que quero identificar uma correlação

corr = ds_tips[['total_bill','tip','size']].corr()

#tracando o heatmap

sns.heatmap(

    corr, annot=True,
    fmt='.2f'

)

plt.show()