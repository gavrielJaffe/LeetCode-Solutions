""""
Input:
DataFrame employees
+---------+--------+
| name    | salary |
+---------+--------+
| Jack    | 19666  |
| Piper   | 74754  |
| Mia     | 62509  |
| Ulysses | 54866  |
+---------+--------+
Output:
+---------+--------+
| name    | salary |
+---------+--------+
| Jack    | 39332  |
| Piper   | 149508 |
| Mia     | 125018 |
| Ulysses | 109732 |
+---------+--------+
"""
import pandas as pd 

data = [
    {"name":"Jack","salary":19666},
    {"name":"Piper","salary":74754},
    {"name":"Mia","salary":62509},
    {"name":"Ulysses","salary":54866},
]

def createDataframe(data):
    return pd.DataFrame(data,columns=["name","salary"])

def modifiySalaryColumn(df):
    df['salary'] = df['salary'] * 2 
    return  df
# Bets 49 %
def modifiySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] = employees['salary'] * 2 
    return employees

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.assign(salary= 2 * employees['salary'])

df = createDataframe(data)
ans = modifySalaryColumn(df)
print(ans)
