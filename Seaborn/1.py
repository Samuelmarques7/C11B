#Fundamentos de Seaborn

import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns


#importando o dataset tips

ds_tips = sns.load_dataset('tips')

#print(ds_tips)

#SEtando um estilo diferente no grafico

sns.set_style('dark')

sns.set_context('talk')
#traçando um scatterplot

sns.scatterplot(data=ds_tips, x='total_bill',y='tip')

plt.xlabel('Conta total em US$')

plt.ylabel('Gorgeta em US$')

plt.show()
