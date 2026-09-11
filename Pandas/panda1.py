#Como preencher uma Series
#lista de labels
# lista de valores

import pandas as pd

import math as mt

import numpy as np

labels = ['Tiago','Mateus','Bruna', 'Julia']

valores = [ 23, 25 , 27, 22]

#Criando valores

se1 = pd.Series(index=labels, data = valores)

print(se1)

print(type(se1))

# Acessando elementos da Series

print(se1['Mateus'])
print(se1[['Mateus','Julia']])


