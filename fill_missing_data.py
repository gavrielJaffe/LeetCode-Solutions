"""DataFrame products
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| name        | object |
| quantity    | int    |
| price       | int    |
+-------------+--------+

Write a solution to fill in the missing value as 0 in the quantity column.

The result format is in the following example.

 

Example 1:
Input:+-----------------+----------+-------+
| name            | quantity | price |
+-----------------+----------+-------+
| Wristwatch      | None     | 135   |
| WirelessEarbuds | None     | 821   |
| GolfClubs       | 779      | 9319  |
| Printer         | 849      | 3051  |
+-----------------+----------+-------+
Output:
+-----------------+----------+-------+
| name            | quantity | price |
+-----------------+----------+-------+
| Wristwatch      | 0        | 135   |
| WirelessEarbuds | 0        | 821   |
| GolfClubs       | 779      | 9319  |
| Printer         | 849      | 3051  |
+-----------------+----------+-------+
"""
import pandas as pd 

data = [
    {"name": "Wristwatch", "quantity": None, "price": 135},
    {"name": "WirelessEarbuds", "quantity": None, "price": 821},
    {"name": "GolfClubs", "quantity": 779, "price": 9319},
    {"name": "Printer", "quantity": 849, "price": 3051}
]

df = pd.DataFrame(data,columns=["name","quantity","price"])

    # products['quantity'][1] = 0 # would make all of the quantity as 0 
    # print(products['quantity'].isnull())

# Beats 21.05% of users with Pandas
def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products = products.fillna({"quantity":0})
    return products
    

ans = fillMissingValues(df)
print(ans)