import pandas as pd
df = pd.read_csv(r"D:\Onediver\OneDrive\Desktop\rental_etl_project\Data\data_raw\houses.csv")
df['price_clean'] = df['price'].str.replace('RM', '').str.replace(',', '').str.replace('','')
print(df[['price','price_clean']].head(10))

# 可视化
import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(10, 6))
sns.histplot(df['price_clean'], bins=30, kde=True)
plt.title('Rent Price Distribution in malaysia')
plt.xlabel('price(RM)')
plt.ylabel('Number of listings')
plt.grid(True)
plt.tight_layout()
plt.show(block=True)