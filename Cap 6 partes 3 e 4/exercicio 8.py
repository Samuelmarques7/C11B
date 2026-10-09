# 8. Por meio do dataset space.csv, após filtrar apenas as missões com custo
# conhecido (Cost > 0), trace um Boxplot comparando a distribuição do custo
# das missões (Cost) entre foguetes com status "StatusActive" e
# "StatusRetired", permitindo identificar mediana, dispersão e outliers de
# cada grupo.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# lendo o dataset space.csv
dfSpace = pd.read_csv('space.csv', delimiter=';')

dfCusto = dfSpace[dfSpace[' Cost'] > 0]

sns.boxplot(data=dfCusto,
            x='Status Rocket',
            y=' Cost'
            )

plt.title("Custo das missões por status do foguete")
plt.show()