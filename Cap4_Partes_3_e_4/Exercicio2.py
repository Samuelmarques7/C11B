# Baseado nos commandos que vimos até
# o momento e no Datasetfornecido, crie scripts em Python que respondam às seguintes
# perguntas:
# 2. Qual a media de gastos de uma missão especial se baseando em
# missões que possuam valores disponíveis (>0)?

import numpy as np

dataset = np.loadtxt('space.csv',delimiter = ';', dtype=str,encoding='utf-8')

#print(dataset[0])

media = 0

for dados in dataset[1:]:

    if float(dados[6]) > 0:
        media = media + float(dados[6])

media = media/(len(dataset)-1)

print (media)
