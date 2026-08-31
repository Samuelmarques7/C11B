# Qual a porcentagem de missões realizadas com foguetes cujo status
# é "StatusRetired " (coluna Status Rocket)?


import numpy as np

dataset = np.loadtxt('space.csv',delimiter=';',dtype=str,encoding='utf-8')

dataset = np.char.strip(dataset)

status_rocket = dataset[1:,5]

cond = status_rocket == 'StatusRetired'

print(f"A porcentagem de missoes realizadas com o status Retired é: {cond.mean()*100:.2f}%")