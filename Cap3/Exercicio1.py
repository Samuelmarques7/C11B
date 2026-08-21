# Crie uma lista preenchida com os 5 primeiros colocados de um
# Campeonato de Futebol, na ordem de colocação. Depois mostre:

times = ['Barcelona','Real Madrid','PSG','Inter','Arsenal']

# a. Apenas os 3 primeiros colocados;

print(times[:3])

# b. Os últimos 2 colocados;

print(times[3:])
# c. Uma lista com os times em ordem alfabética;

times.sort()
print(times)

# d. Em que posição da tabela se encontra o Barcelona

print(times.index('Barcelona'))