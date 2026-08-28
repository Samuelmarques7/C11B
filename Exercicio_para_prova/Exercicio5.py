#Encontre qual páis da América do Sul e Caribe(LATIN AMER &
# CARIB) possui a maior renda per capita(GDP($ per capita));

import numpy as np

dataset = np.loadtxt('paises.csv', delimiter=';', dtype=str, encoding='utf-8')


dataset = np.char.strip(dataset) # Remove espaços extras dos valores do dataset

colum_region = dataset[1:, 1] # Pega a coluna de regiões, ignorando a primeira linha

cond = colum_region == 'LATIN AMER. & CARIB' # Cria uma condição para selecionar apenas os países da região "LATIN AMER. & CARIB"

coluna_renda_per_capita = dataset[1:, 8].astype(float) # Pega a coluna de renda per capita e converte os valores para float

paises = dataset[1:, 0][cond] # Seleciona apenas os países que atendem à condição criada anteriormente

rendas = coluna_renda_per_capita[cond] # Seleciona apenas as rendas per capita dos países da região

indice_maior = np.argmax(rendas) # Encontra o índice (posição) do maior valor de renda

pais_maior_renda = paises[indice_maior]

print(f"A maior renda per capita da América do Sul e Caribe pertence ao país: {pais_maior_renda}")
