# 4. Crie uma matriz de tamanho qualquer. Extraia seu número de linhas
# e colunas, multiplique -os, e diga se esta matriz poderia se tornar um vetor
# unidimensional com número par ou ímpar de elementos

import numpy as np

mtz = np.random.randint(0,10,[3,2])

print(mtz)

linha,coluna = mtz.shape

total = linha * coluna

print(total)

print(linha)