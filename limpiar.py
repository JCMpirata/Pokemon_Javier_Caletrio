from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
import pandas as pd

df = pd.read_csv('pokemon.csv')

# Crea un objeto SimpleImputer para reemplazar los valores faltantes con la media de la columna
imputer = SimpleImputer(strategy='mean')

# Aplica la imputación a las columnas numéricas del DataFrame
df[['column 1', 'column 2']] = imputer.fit_transform(df[['column 1', 'column 2']])

# Guarda el DataFrame limpio en un nuevo archivo CSV
df.to_csv('pokemon_limpiado.csv', index=False)


df = pd.read_csv('pokemon.csv')

# Crea un objeto StandardScaler para escalar los valores numéricos
scaler = StandardScaler()

# Aplica el escalado a las columnas numéricas del DataFrame
df[['columna1', 'columna2']] = scaler.fit_transform(df[['columna1', 'columna2']])

# Guarda el DataFrame limpio en un nuevo archivo CSV
df.to_csv('pokemon_limpiado.csv', index=False)


df = pd.read_csv('pokemon.csv')

# Crea un objeto OneHotEncoder para codificar las variables categóricas
encoder = OneHotEncoder()

# Aplica la codificación a la columna 'categoria' del DataFrame
categorias_codificadas = encoder.fit_transform(df[['categoria']])

# Concatena las columnas codificadas al DataFrame original
df = pd.concat([df, categorias_codificadas], axis=1)

# Elimina la columna original 'categoria'
df.drop(['categoria'], axis=1, inplace=True)

# Guarda el DataFrame limpio en un nuevo archivo CSV
df.to_csv('pokemon_limpiado.csv', index=False)







