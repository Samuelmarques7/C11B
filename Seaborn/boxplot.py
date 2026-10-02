
import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns


#importando o dataset tips

ds_tips = sns.load_dataset('tips')

# tracando um boxplot

sns.boxplot (
    data=ds_tips,
    x='day',
    y = 'tip',
    hue = 'sex'
)

plt.show()