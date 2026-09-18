import numpy as np

import pandas as pd

# 6. Utilizando do DataFrame exemplo do tópico 5.3 deste material, calcule a
# média dos elementos da coluna X que são menores que 30;


# criando um dataframe
df = pd.DataFrame(
index=['A', 'B', 'C', 'D', 'E'],
columns=['W', 'X', 'Y', 'Z'],
data=np.random.randint(1, 50, [5, 4]))

print(df)
print(df[df['X'] < 30]['X'].mean())

# 7. Utilizando do mesmo DataFrame, apresente a média dos elementos da
# linha D usando a função loc() como base e a soma dos elementos da linha E
# usando a função iloc() como base;


# média da linha D, com loc (seleciona por label)
print(df.loc['D'].mean())

# soma da linha E, com iloc (seleciona por posição)
print(df.iloc[4].sum())



# 8. Faça um Slicing na matriz mostrando apenas as linhas A, C e E
# juntamente com as colunas X e Y. Em seguida, mostre qual seria a soma dos
# elementos de cada uma destas linhas e cada uma destas colunas.

# realizando um slicing com loc()
print(df.loc[['A', 'B','E'], ['X', 'Y']])

print(f"Soma da linha A: {df.loc['A'].sum()}")
print(f"Soma da linha B: {df.loc['B'].sum()}")
print(f"Soma da linha E: {df.loc['E'].sum()}")

print(f"Soma da coluna X: {df['X'].sum()}")
print(f"Soma da coluna Y: {df['Y'].sum()}")
