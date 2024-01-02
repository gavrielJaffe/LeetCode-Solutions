# a = (1,2)
# a+=(3)
# print(a)



import pandas as pd

data = {
    'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Value': [1, 2, 3, 4, 5, 6]
}
df = pd.DataFrame(data)
print(df)

pivot = df.pivot_table(index='Category', values='Value', aggfunc='max')
pivot = df.pivot_table(index='Category', values='Value', aggfunc='max')
print(pivot)
