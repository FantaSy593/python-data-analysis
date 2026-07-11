import pandas as pd

sales_data = {
    'order_id': [1, 2, 3, 4, 5, 6, 7],
    'category': ['Электроника', 'Одежда', 'Электроника', 'Книги', 'Одежда', 'Книги', 'Электроника'],
    'revenue': [25000, 3200, 15000, 850, 4100, 1200, 89000]
}
df = pd.DataFrame(sales_data)

category_report = df.groupby('category').agg(
    total_orders=('order_id', 'count'),
    total_revenue=('revenue', 'sum'),
    average_check=('revenue', 'mean')
).reset_index()

category_report = category_report.sort_values(by='total_revenue', ascending=False)

print(category_report)
