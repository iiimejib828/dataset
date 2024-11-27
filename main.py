import pandas as pd

df = pd.read_csv('StudentGradesAndPrograms.csv')

print(df.head())
print(df.info())
print(df.describe())

df = pd.read_csv('dz.csv')
df = df.fillna({col: 'Неизвестно' for col in df.select_dtypes(include='object')})
group = df.groupby('City')['Salary'].mean()
print(f'\nСредняя зарплата по {group}')
