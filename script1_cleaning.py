import pandas as pd


data = {
    'user_id': [101, 102, 103, 101, 105, 106],
    'page_views': [15, 22, None, 15, 8, 45],
    'purchase_amount': [1200, None, 450, 1200, 300, 5800]
}
df = pd.DataFrame(data)
print("Исходный датафрейм:")
print(df)


df = df.drop_duplicates()

df['page_views'] = df['page_views'].fillna(df['page_views'].mean())

df['purchase_amount'] = df['purchase_amount'].fillna(0)

print("\nДанные после очистки и обработки пропусков:")
print(df)
