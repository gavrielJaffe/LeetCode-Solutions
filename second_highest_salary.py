import pandas as pd

data = {
    'id': [1, 2, 3],
    'salary': [100, 200, 300]
} # Outpot 200


data2 = {
    'id': [1],
    'salary': [100]
} # Outpot None

data3 = {
    'id': [1, 2, 3],
    'salary': [100, 100, 100]
} # Outpot None

data4 = {
    'id': [1, 2, 3],
    'salary': [100, 100, 50]
} # Outpot 50

data5 = {
    'id': [1, 2, 3,4,5],
    'salary': [100, 100, 50,30,20]
    # 'salary': [100, 100, 50,30,20] -> [50,30,20]
} # Outpot 50


employee_df = pd.DataFrame(data5)
print(employee_df)

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    max_salary = employee['salary'].max()
    max_salary_index = employee['salary'].idxmax()
    employee = employee.drop([max_salary_index]) # not all of the use cases are falling in. data5 , data4
    employee = employee['salary'].max()
    if max_salary == employee: # in case of two employee in the same salary we would send null
        employee = None
    return pd.DataFrame({employee},columns=["SecondHighestSalary"])

ans = second_highest_salary(employee_df)
print(ans)
