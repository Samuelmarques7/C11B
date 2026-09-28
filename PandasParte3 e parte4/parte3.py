import pandas as pd

import numpy as np

# 1. Carregue o Dataset paises.csv e em seguida mostre:
# a. Quais são os países da OCEANIA;
# b. Quantos países são da OCEANIA;
# Dica: para busca de padrões textuais no Pandas, use métodos da subclasse str da
# Series. Ex: series.str.contains('texto')

ds = pd.read_csv('paises.csv', sep=';')

# retirando os espaços que sobram nos nomes e nas regiões
ds['Country'] = ds['Country'].str.strip()
ds['Region'] = ds['Region'].str.strip()

paises_oceania = ds[ds['Region'].str.contains('OCEANIA')]['Country']

print(f"Países da OCEANIA:\n{paises_oceania}\n")

print(f"Quantidade de países da OCEANIA: {paises_oceania.count()}\n")

# 2. Encontre o nome e a região do país que possui a maior população segundo este
# Dataset;

# idxmax() retorna o index da linha que tem o maior valor
maior_populacao = ds.loc[ds['Population'].idxmax(), ['Country', 'Region']]

print(f"País com a maior população:\n{maior_populacao}\n")

# 3. Agrupe os países por Regiões. Em seguida, mostre a média de alfabetização
# (Literacy (%)) de cada região do planeta;

group_region = ds.groupby('Region')

print(f"Média de alfabetização de cada região:\n{group_region['Literacy (%)'].mean()}\n")

# 4. Busque o nome de todos os países do Dataset que não possuem costa marítima
# (Coastline (coast/area ratio) == 0) e guarde-os em um novo arquivo chamado
# noCoast.csv;

sem_costa = ds[ds['Coastline (coast/area ratio)'] == 0]['Country']

print(f"Países sem costa marítima:\n{sem_costa}\n")

sem_costa.to_csv('noCoast.csv', sep=';')

# 5. Faça uma função que receba a taxa de mortalidade de cada país (Deathrate) e
# retorne o texto 'Balanced' caso o valor seja < 9 e 'Urgent' caso contrário. Em
# seguida, crie um campo no Dataset chamado 'Humanitarian Help' que receba estes
# valores para cada país. No final, mostre o Dataset para verificar se a inserção da nova
# coluna foi feita com sucesso.

def ajudaHumanitaria (x):
    if x < 9:
        return 'Balanced'
    else:
        return 'Urgent'

ds['Humanitarian Help'] = ds['Deathrate'].apply(ajudaHumanitaria)

print(ds[['Country', 'Deathrate', 'Humanitarian Help']])
