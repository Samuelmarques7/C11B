import pandas as pd

import numpy as np

import math as mt

#SLICING DE DADOS NO DATAFRAME COM LOC (LABELS) E ILOC (INDICES

#Como preencher um Dataframe
# Lista de labels (Coluna)

colunas = ['W','X','Y','Z']

# Lista de labels (Linhas)

linhas = ['A','B','C','D','E']

np.random.seed(10)

# Lita de valores

valores = np.random.randint(1,50,[5,4])

df = pd.DataFrame(columns=colunas,
                  index = linhas,
                  data=valores)


#PUXANDO UMA UNICA LINHA DO DATAFRAME

#print(df.loc['C',['W','X','Y','Z']])

print(df.iloc[2,:])

# PUXANDO MULTIPLAS LINHAS

print(df.loc[['B','E'],['W','X','Y','Z']])

print(df.iloc[[1,4],:])

#puxando a matriz 2x2 do canto inferior direito

print(df.loc[['D','E'],['Y','Z']])

print(df.iloc[[3,4],[2,3]])

