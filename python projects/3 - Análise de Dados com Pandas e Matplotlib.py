import pandas as pd
import matplotlib.pyplot as plt

# Carrega o CSV e faz limpeza de dados
df = pd.read_csv('dados.csv')
df.dropna(inplace=True)

# Plotando dados específicos
df['coluna_de_interesse'].plot(kind='line', title='Crescimento ao Longo do Tempo')
plt.xlabel('Tempo')
plt.ylabel('Valor')
plt.grid(True)
plt.show()

# Estatísticas básicas
media = df['coluna_de_interesse'].mean()
print(f"Média: {media}")
