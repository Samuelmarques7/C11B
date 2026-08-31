# Baseado nos commandos que vimos até o momento e no Dataset
# fornecido , crie scripts em Python que respondam às seguintes perguntas:
# 1. Apresente a porcentagem de missões que deram certo

import numpy as np

dataset = np.loadtxt('space.csv',delimiter=';',dtype=str,encoding='utf-8')

dataset = np.char.strip(dataset)

status_rocket = dataset[1:,7]

cond = status_rocket == 'Success'

quant_success = np.sum(cond)

total_mission = len(status_rocket)

porcentagem = quant_success/total_mission * 100

print(f"A porcentagem de missões que deram certo é: {porcentagem:.2f}%")

#A porcentagem de missoes que deram certo é o numero de missoes que deram certo dividio pelo total de missoes