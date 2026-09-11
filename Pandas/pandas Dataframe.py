import numpy as np
import pandas as pd

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

print(df)

#MANIPULANDO O DATAFRAME

#PUXANDO UMA UNIC COLUNA DO DATAFRAME

print(df['X'])

#PUXANDO DUAS COLUNAS DO DATAFRAME

print(df[['Y','Z']])

#PUXANSO UMA UNICA CELULA

print (df['Y']['C'])


#PUXANDO MULTIPLAS COLUNAS

print(df[['W','X','Z']])