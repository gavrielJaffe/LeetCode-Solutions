import pandas as pd

data = {
    'id': [1, 2, 3, 4, 5, 6],
    'name': ['Will', 'Jane', 'Alex', 'Bill', 'Zack', 'Mark'],
    'referee_id': [None, None, 2, None, 1, 2]
}
df = pd.DataFrame(data)

# not expected in Leetcode , but give the right output . 
def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    mask = (customer['referee_id'] == 2)
    customer = customer[~mask][['name']]
    return customer

# works 
def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    x = customer[(customer['referee_id'] != 2)][['name']].reset_index()
    return pd.DataFrame(x[['name']])

ans = find_customer_referee(customer=df)
print(type(ans))
print(ans)
