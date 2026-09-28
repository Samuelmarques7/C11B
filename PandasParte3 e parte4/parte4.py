import pandas as pd

import numpy as np

ds = pd.read_csv('paises.csv', sep=';')

# 6. Agrupe os países por região e mostre as estatísticas descritivas da coluna
# Population de cada região. Em seguida, mostre apenas as 5 primeiras linhas
# deste resultado;

group_region = ds.groupby('Region')

estatisticas = group_region['Population'].describe()

print(f"Estatísticas descritivas da população de cada região:\n{estatisticas}\n")

print(f"5 primeiras linhas:\n{estatisticas.head(5)}\n")

# 7. Crie uma função customizada que receba a coluna Infant mortality (per 1000
# births) de um país e retorne o valor reduzido em 15% (simulando assim uma meta
# de redução da mortalidade infantil). Aplique esta função à coluna usando o
# método apply() e, em seguida, concatene a coluna original com a coluna
# resultante lado a lado para se fazer uma comparação;

def reduz15 (x):
    return x * 0.85

mortalidade1 = ds['Infant mortality (per 1000 births)']

mortalidade2 = mortalidade1.apply(reduz15)

# renomeando a nova series pra não ficar com o mesmo nome da original
mortalidade2.name = 'Infant mortality -15%'

print(pd.concat([mortalidade1, mortalidade2], axis=1))

# 8. Remova a coluna Coastline (coast/area Ratio) do dataset. Em seguida, salve
# este novo dataset em um arquivo chamado paises_sem_coastline.csv.

# axis = 1 para excluir coluna
ds_sem_coastline = ds.drop('Coastline (coast/area ratio)', axis=1)

print(ds_sem_coastline.columns)

ds_sem_coastline.to_csv('paises_sem_coastline.csv', sep=';')
