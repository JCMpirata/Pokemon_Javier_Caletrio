# limpiar el archivo pokemon.csv con la library pandas y sklearn para que quede como pokemon_limpiado.csv
#


import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder

df = pd.read_csv('pokemon.csv')

# Crea un objeto SimpleImputer para reemplazar los valores faltantes con la media de la columna
imputer = SimpleImputer(strategy='mean')

# Aplica la imputación a las columnas numéricas del DataFrame
df[['hp', 'attack', 'defense', 'sp_attack', 'sp_defense', 'speed']] = imputer.fit_transform(df[['hp', 'attack', 'defense', 'sp_attack', 'sp_defense', 'speed']])

# Guarda el DataFrame limpio en un nuevo archivo CSV
df.to_csv('pokemon_limpiado.csv', index=False)  # index=False para que no se guarde el indice del dataframe

df = pd.read_csv('pokemon.csv')

# Crea un objeto StandardScaler para escalar los valores numéricos
scaler = StandardScaler()

# Aplica el escalado a las columnas numéricas del DataFrame
df[['hp', 'attack', 'defense', 'sp_attack', 'sp_defense', 'speed']] = scaler.fit_transform(df[['hp', 'attack', 'defense', 'sp_attack', 'sp_defense', 'speed']])

# Guarda el DataFrame limpio en un nuevo archivo CSV
df.to_csv('pokemon_limpiado.csv', index=False)

df = pd.read_csv('pokemon.csv')

# Crea un objeto OneHotEncoder para codificar las variables categóricas
encoder = OneHotEncoder()

# Aplica la codificación a la columna 'categoria' del DataFrame
categorias_codificadas = encoder.fit_transform(df[['categoria']])
# print(categorias_codificadas)

# Concatena las columnas codificadas al DataFrame original
df = pd.concat([df, categorias_codificadas], axis=1)

# Elimina la columna original 'categoria'
df.drop(['categoria'], axis=1, inplace=True)

# Guarda el DataFrame limpio en un nuevo archivo CSV
df.to_csv('pokemon_limpiado.csv', index=False)


