import pandas as pd 
"""
Input: 
DataFrame animals:
+----------+---------+-----+--------+
| name     | species | age | weight |
+----------+---------+-----+--------+
| Tatiana  | Snake   | 98  | 464    |
| Khaled   | Giraffe | 50  | 41     |
| Alex     | Leopard | 6   | 328    |
| Jonathan | Monkey  | 45  | 463    |
| Stefan   | Bear    | 100 | 50     |
| Tommy    | Panda   | 26  | 349    |
+----------+---------+-----+--------+
Output: 
+----------+
| name     |
+----------+
| Tatiana  |
| Jonathan |
| Tommy    |
| Alex     |
+----------+
Explanation: 
All animals weighing more than 100 should be included in the results table.
Tatiana's weight is 464, Jonathan's weight is 463, Tommy's weight is 349, and Alex's weight is 328.
The results should be sorted in descending order of weight.
"""
data = [
    {"name": "Tatiana", "species": "Snake", "age": 98, "weight": 464},
    {"name": "Khaled", "species": "Giraffe", "age": 50, "weight": 41},
    {"name": "Alex", "species": "Leopard", "age": 6, "weight": 328},
    {"name": "Jonathan", "species": "Monkey", "age": 45, "weight": 463},
    {"name": "Stefan", "species": "Bear", "age": 100, "weight": 50},
    {"name": "Tommy", "species": "Panda", "age": 26, "weight": 349},
]
df = pd.DataFrame(data)

# Beats 18.5% using pd
# def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
#     animals = animals[animals['weight'] > 100].sort_values(by=['weight'], ascending=False)
#     df = pd.DataFrame (animals['name'])
#     return df

# Beats 99.58 % of users with Pandas
def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    animals = animals[animals['weight'] > 100].sort_values(by=['weight'], ascending=False)
    return pd.DataFrame(animals['name'])
  
# Beats 88.75%of users with Pandas
# def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
#     animals = animals.loc[animals['weight']>100].sort_values(by='weight',ascending=False)
#     return pd.DataFrame(animals['name'])

ans = findHeavyAnimals(df)
# print(ans)