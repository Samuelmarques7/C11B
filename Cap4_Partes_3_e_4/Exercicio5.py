# Mostre o nome das empresas que já realizaram missões espaciais,
# juntamente com suas respectivas quantidades de missões (use
# o for no final para mostrar as informações)


import numpy as np

dataset = np.loadtxt('space.csv',delimiter=';',dtype=str,encoding='utf-8')

dataset = np.char.strip(dataset)

company = dataset[1:,1]

empresas,quantidade = np.unique(company,return_counts=True)

for empresas,quantidade in zip(empresas,quantidade):
    print(f"{empresas} : {quantidade} missões")