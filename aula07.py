# import pandas as pd
# df = pd.read_csv('nao_residencial.csv', encoding='utf-8', usecols=3)
# print(df.head(10))


# Exemplo de merge (consulta) no Python
import pandas as pd

# O segredo é usar o sep=';' para o Pandas separar as colunas corretamente
# df_naoresid = pd.read_csv('nao_residencial.csv', sep=';')
df_resid = pd.read_csv('residencial.csv', sep=';')


print(df_resid['codbairro','bairro'].head(10))

# print(df_naoresid['bairro'].head(10))