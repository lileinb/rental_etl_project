import pandas as pd
df = pd.read_csv(r"D:\Onediver\OneDrive\Desktop\rental_etl_project\Data\data_raw\houses.csv")

print('前五行数据\n', df.head())
print('查看数据维度\n', df.shape)
print("数据概况查看\n", df.info())
print('描述性统计\n', df.describe())   
print('查看缺失值\n', df.isnull().sum())
print('查看数据类型\n',df.dtypes)
print('查看数据列名\n',df.columns)




