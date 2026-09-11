import numpy as np

nomes1 = np.array(["Ana", "Bruno", "Carla", "Diego"])
nomes2 = np.array(["Elisa", "Fábio", "Gustavo", "Helena"])

concatenado = np.concatenate((nomes1, nomes2))
print("Concatenado:", concatenado)

array_2d = concatenado.reshape(2, 4)
print("\nArray 2D (2x4):")
print(array_2d)

array_2d_desc = np.sort(array_2d, axis=None)[::-1].reshape(2, 4)
print("\nArray 2D em ordem decrescente:")
print(array_2d_desc)