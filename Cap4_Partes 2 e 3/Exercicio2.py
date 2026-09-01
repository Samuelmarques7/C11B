# Crie dois NumPy Arrays unidimensionais:
# um de números pares de 0 à 51 e outro também de números pares de 100 até 50.
# Em seguida, os concatenee mostre os resultados ordenados

import numpy as np

arr = np.arange(0,51,2)

arr2 = np.arange(100,49,-2)

arr3 = np.concatenate((arr,arr2))

print(np.sort(arr3))
