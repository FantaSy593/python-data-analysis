import pandas as pd
import numpy as np

marketing_data = {
    'user_id': [201, 202, 203, 204, 205],
    'clicks': [10, 50, 5, 100, 0],
    'conversions': [1, 8, 0, 25, 0]
}
df = pd.DataFrame(marketing_data)

df['conversion_rate'] = np.where(
    df['clicks'] > 0, 
    (df['conversions'] / df['clicks']) * 100, 
    0.0
)

high_active_users = df[df['conversion_rate'] > 15.0]

print(df)
print(high_active_users)
