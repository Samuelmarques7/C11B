
import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns


#importando o dataset tips

ds_tips = sns.load_dataset('tips')

sns.regplot(
    data=ds_tips,
    x = 'total_bill',
    y = 'tip',
    line_kws={'color':'red'}
)

plt.show()