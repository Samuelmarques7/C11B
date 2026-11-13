import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from statsmodels.tsa.seasonal import seasonal_decompose

# EXERCÍCIO 1 - Cap. 7
# SÉRIE 1 - airtravel.csv
# Número mensal de passageiros de avião (1958-1960)
air = pd.read_csv('airtravel.csv', parse_dates=['Date'], index_col='Date')
air = air[['Passengers']].astype(float).asfreq('MS')

# Plotando a série temporal
air['Passengers'].plot(figsize=(10, 5),
                       title='Passageiros de avião por mês (1958-1960)',
                       xlabel='Data', ylabel='Passageiros')
plt.tight_layout()
plt.show()

decomp_air = seasonal_decompose(air['Passengers'], model='multiplicative', period=12)
decomp_air.plot()
plt.tight_layout()
plt.show()

print('--- airtravel ---')
print('Tendência (média anual aproximada):')
print(air['Passengers'].resample('YS').mean().round(1))
print('Fator sazonal médio por mês:')
print(decomp_air.seasonal[:12].round(3))

# RESPOSTAS - SÉRIE 1 airtravel
# a. A série possui tendência? Se sim, que tipo?
#    Sim. Tendência CRESCENTE: a média de passageiros sobe de um ano para o
#    outro (1958 ~ 381, 1959 ~ 428, 1960 ~ 476 passageiros/mês), com
#    crescimento aproximadamente constante em direção ao final da série.
#
# b. A série possui sazonalidade? Se sim, qual o período que ela acontece?
#    Sim. Sazonalidade ANUAL, com período de 12 meses (o padrão se repete a
#    cada ano). Há picos em julho e agosto (férias de verão) e vales em
#    novembro e fevereiro. A amplitude sazonal aumenta com o nível da série,
#    por isso a decomposição multiplicativa foi usada.
#
# c. A série apresenta um Ciclo? Se sim, por qual razão?
#    Não. Os dados cobrem apenas 3 anos, e o padrão que se repete é o ano
#    calendário (sazonalidade), não uma flutuação de longo prazo sem período
#    fixo (ciclo). Para identificar um ciclo econômico seriam necessários
#    dados por vários anos.


# --------------------------------------------------------------------------
# SÉRIE 2 - co2_emissions.csv
# --------------------------------------------------------------------------
co2 = pd.read_csv('co2_emissions.csv', index_col='Year')
co2.index = pd.to_datetime(co2.index.astype(str), format='%Y')  # índice temporal anual

# Plotando a série temporal
co2['CO2_Emissions'].plot(figsize=(10, 5),
                          title='Emissões de CO2 (1990-2020)',
                          xlabel='Ano', ylabel='Emissões de CO2')
plt.tight_layout()
plt.show()

trend_co2 = co2['CO2_Emissions'].rolling(window=5, center=True).mean()
resid_co2 = co2['CO2_Emissions'] - trend_co2

fig, axes = plt.subplots(3, 1, figsize=(10, 9), sharex=True)
co2['CO2_Emissions'].plot(ax=axes[0], title='Observado')
trend_co2.plot(ax=axes[1], title='Tendência (média móvel 5 anos)')
resid_co2.plot(ax=axes[2], title='Resíduo (ruído / oscilações)')
plt.tight_layout()
plt.show()

print('--- co2_emissions ---')
print(co2['CO2_Emissions'].round(1).to_string())

# RESPOSTAS - SÉRIE 2
# a. A série possui tendência? Se sim, que tipo?
#    Sim. Tendência DECRESCENTE no período completo: sai de ~101 em 1990 e
#    chega a ~39 em 2020. Ela não é linear: há fases de alta (1990-1992,
#    2004-2007, 2014-2015) intercaladas com quedas maiores (1993-2003,
#    2008-2013, 2016-2020).
#
# b. A série possui sazonalidade? Se sim, qual o período que ela acontece?
#    Não. Os dados são anuais (um valor por ano), então não existe padrão
#    que se repita dentro do ano. Não há um período sazonal identificável.
#
# c. A série apresenta um Ciclo? Se sim, por qual razão?
#    Sim. Após remover a tendência, sobram oscilações de médio prazo, com
#    altos em torno de 1993, 1999-2000, 2007 e 2015-2017 e baixos em torno de
#    1995, 2003-2004 e 2011-2013 (valores obtidos do resíduo calculado acima;
#    a média móvel centrada de 5 anos não cobre 2019-2020). Esses ciclos não
#    têm período fixo (intervalos de ~7 a 9 anos entre picos/vales), o que os diferencia da
#    sazonalidade. A causa mais provável são eventos externos e
#    econômicos (expansões e recessões, como a crise de 2008 e o período de
#    retração recente), mas o arquivo não traz informações que confirmem
#    essa explicação, então ela é uma hipótese.
