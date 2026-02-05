import pandas as pd
df = pd.read_csv('residencial.csv', encoding='utf-8')

df.to_csv('residencial_limpo2.csv', encoding='utf-8', index=False)