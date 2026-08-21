# Baseado nos commandos que vimos até o momento e no Dataset
# fornecido , crie scripts em Python que respondam às seguintes perguntas:
# 1. Apresente a porcentagem de missões que deram certo

import numpy as np

dataset = np.loadtxt('space.csv',delimiter = ';', dtype=str,encoding='utf-8')

missoes = 0

#print(dataset[0])

for dados in dataset:
    if dados[7] == 'Success':
         missoes += 1

porcentagem = (missoes/(len(dataset)-1)) *100

print(porcentagem)