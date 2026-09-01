# 1. Crie dois NumPy Arrays unidimensionais de tamanho
# 8: um formado apenas por 1’s e outro formado por números aleatórios entre
# 0 e 9. Some estes dois NumPy Arrays e guarde
# o resultado dentro de um terceiro NumPy Array. Por
# fim, faça o seguinte:
# a. Se a soma de todos os elementos do Array resultante for >= 40, remodele este NumPy
# Array para se tornar uma matriz com mais linhas do que colunas
# . Senão, remodele para que se torne uma matriz com mais colunas do que linhas.

import numpy as np

arr = np.ones(8)

arr2 = np.random.randint(0,10,8)

arr3 = arr + arr2

soma = np.sum(arr3)

if soma >= 40:
    mtz = arr3.reshape(4,2)
else:
    mtz = arr3.reshape(2,4)

print(f"Soma = {soma}")
print(mtz)