import pandas as pd 
from typing import List
"""
2880. Select Data 
Example 1:
Input:
+------------+---------+-----+
| student_id | name    | age |
+------------+---------+-----+
| 101        | Ulysses | 13  |
| 53         | William | 10  |
| 128        | Henry   | 6   |
| 3          | Henry   | 11  |
+------------+---------+-----+
Output:
+---------+-----+
| name    | age | 
+---------+-----+
| Ulysses | 13  |
+---------+-----+

"""
data = [
    {'student_id': 101, 'name': 'Ulysses', 'age': 13},
    {'student_id': 53, 'name': 'William', 'age': 10},
    {'student_id': 128, 'name': 'Henry', 'age': 6},
    {'student_id': 3, 'name': 'Henry', 'age': 11}
]
students = pd.DataFrame(data)
# 
def selectData(students: pd.DataFrame) -> pd.DataFrame:
    columns_name = ["name","age"]
    return students.loc[students['student_id'] == 101][columns_name]

print(selectData(students))