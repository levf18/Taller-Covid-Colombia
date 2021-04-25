import pandas as pd
import numpy as np

url = "Casos_positivos_de_COVID-19_en_Colombia.csv"
df = pd.read_csv(url)

df.loc[df['Recuperado'] ==
       'fallecido', 'Recuperado'] = 'Fallecido'
df.loc[df['Estado'] ==
       'leve', 'Estado'] = 'Leve'
df.loc[df['Estado'] ==
       'LEVE', 'Estado'] = 'Leve'
df.loc[df['Ubicación del caso'] ==
       'CASA', 'Ubicación del caso'] = 'Casa'

df.loc[df['Ubicación del caso'] ==
       'casa', 'Ubicación del caso'] = 'Casa'
df.loc[df['Sexo'] ==
       'm', 'Sexo'] = 'M'
df.loc[df['Sexo'] ==
       'f', 'Sexo'] = 'F'
# 1. Número de casos de Contagiados en el País
df[df['Recuperado'] == 'Activo'].shape[0]
# 2. Número de Municipios Afectados
df['Nombre municipio'].value_counts().count()
# 4. Número de personas que se encuentran en atención en casa
df[df['Ubicación del caso'] == 'Casa'].shape[0]
# 5. Número de personas que se encuentran recuperados
df[df['Recuperado'] == 'Recuperado'].shape[0]
# 6. Número de personas que ha fallecido
df[df['Estado'] == 'Fallecido'].shape[0]
# 7. Ordenar de Mayor a menor por tipo de caso (Importado, en estudio,
# Relacionado)
df['Tipo de contagio'].value_counts().sort_values(ascending=False)
# 8. Número de departamentos afectados
df['Nombre departamento'].value_counts().count()
# 9. Liste los departamentos afectados(sin repetirlos)
df['Nombre departamento'].value_counts()
# 11. Liste de mayor a menor los 10 departamentos con mas casos de
# contagiados
df[df['Recuperado'] ==
   'Activo']['Nombre departamento'].value_counts().head(10)
# 12. Liste de mayor a menor los 10 departamentos con mas casos de
# fallecidos
df[df['Estado'] ==
   'Fallecido']['Nombre departamento'].value_counts().head(10)
# 13. Liste de mayor a menor los 10 departamentos con mas casos de
# recuperados
df[df['Recuperado'] ==
   'Recuperado']['Nombre departamento'].value_counts().head(10)
# 14. Liste de mayor a menor los 10 municipios con mas casos de
# contagiados
df[df['Recuperado'] ==
   'Activo']['Nombre municipio'].value_counts().head(10)
# 15. Liste de mayor a menor los 10 municipios con mas casos de
# fallecidos
df[df['Estado'] ==
   'Fallecido']['Nombre municipio'].value_counts().head(10)
# 16. Liste de mayor a menor los 10 municipios con mas casos de
# recuperados
df[df['Recuperado'] ==
   'Recuperado']['Nombre municipio'].value_counts().head(10)
# 18. Número de Mujeres y hombres contagiados por ciudad por
# departamento
df.groupby(['Sexo', 'Nombre departamento', 'Nombre municipio']).size()
