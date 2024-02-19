import pandas as pd 

data = {
    'empId': [3, 1, 2, 4],
    'name': ['Brad', 'John', 'Dan', 'Thomas'],
    'supervisor': [None, 3, 3, 3],
    'salary': [4000, 1000, 2000, 4000]
}

data_bonus = {
    'empId': [2, 4],
    'bonus': [500, 2000]
}

df_bonus = pd.DataFrame(data_bonus)
df_emp = pd.DataFrame(data)
# name and bonus amount of each employee with a bonus less than 1000
"""
Output: 
+------+-------+
| name | bonus |
+------+-------+
| Brad | null  |
| John | null  |
| Dan  | 500   |
"""
def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    result = pd.merge(employee,bonus, how="left",on="empId")
    return result[(result['bonus']< 1000) | (result['bonus'].isna())][['name','bonus']]

res = employee_bonus(df_emp ,df_bonus)
print(res)