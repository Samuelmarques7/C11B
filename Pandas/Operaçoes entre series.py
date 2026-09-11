import pandas as pd

import numpy as np

import math as mt

s1 = pd.Series ({'v1':10,'v2':45,'v3':70})
s2 = pd.Series ({'v1':10,'v4':50,'v3':70})

#print(s1,s2)

print(s1 + s2)

print(s1.add(s2, fill_value=0))