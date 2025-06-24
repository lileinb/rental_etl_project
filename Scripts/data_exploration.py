import pandas as pd
df = pd.read_csv('data/raw_data/houses.csv')

print("\n前五行数据")
print(df.head())

print("\n数据维度（行列）:",df.shape)

print("\n数据类型：")
print(df.dtypes)

print("\n 数据字段和数据类型：",df.info())

print("\n缺失值数量：")
print(df.isnull().sum())

