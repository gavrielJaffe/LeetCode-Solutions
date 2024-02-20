import pandas as pd

data = {
    'id': [1, 2, 3, 4, 5, 6],
    'name': ['Will', 'Jane', 'Alex', 'Bill', 'Zack', 'Mark'],
    'referee_id': [None, None, 2, None, 1, 2]
}
df = pd.DataFrame(data)

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    mask = customer['referee_id'] == 2
    customer = customer[~mask]
    df = customer[['name']]
    return df 

ans = find_customer_referee(customer=df)
print(ans)
