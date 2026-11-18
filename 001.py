import pandas as pd

# Para arquivos CSV:
df = pd.read_csv('carros_planilha.csv')

# Para arquivos Excel (.xlsx):
# df = pd.read_excel('seu_arquivo.xlsx')

# Exibe as 5 primeiras linhas no terminal:
print(df.head(5))
