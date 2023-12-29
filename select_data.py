import pandas as pd 
from typing import List
"""
2880. Select Data 


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
# Best way Beats 95.71% of users with Pandas
def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students.loc[students['student_id'] == 101][["name","age"]]



print(selectData(students))