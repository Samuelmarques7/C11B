#Fundamentos de Seaborn

import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

#Histrograma

#importando o dataset tips

ds_penguins = sns.load_dataset('penguins')

print(ds_penguins.columns)

#tracando o histrograma

sns.histplot(data = ds_penguins,  x='flipper_length_mm' , hue = 'species', kde= True)



