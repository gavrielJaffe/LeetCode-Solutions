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

employee_df = pd.DataFrame(data4)
print(employee_df)

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    max_salary = employee['salary'].max()
    max_salary_index = employee['salary'].idxmax()
    employee = employee.drop([max_salary_index])
    employee = employee['salary'].max()
    if max_salary == employee: # in case of two employee in the same salary we would send null
        employee = None
    return pd.DataFrame({employee},columns=["SecondHighestSalary"])

ans = second_highest_salary(employee_df)
print(ans)

# def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
#     max_salary = employee['salary'].max()
#     max_salary_index = employee['salary'].idxmax()
#     employee = employee.drop([max_salary_index])
#     employee = employee['salary'].max()
#     if max_salary == employee: # in case of two employee in the same salary we would send null
#         employee = None
#     df = pd.DataFrame({employee},columns=["SecondHighestSalary"])
#     return df 