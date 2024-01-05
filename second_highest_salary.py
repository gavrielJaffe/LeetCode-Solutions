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
    'id': [1,2,3,4],
    'salary': [100, 100, 100,100]
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


employee_df = pd.DataFrame(data3)

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    # find all of the indexes of the max_salary in the df.
    max_salary = employee['salary'].max()
    # print(max_salary)
    indexs_of_max_salary = (employee[employee['salary'] == max_salary].index).tolist()
    # drop of indexs_of_max_salary,saved to the df.delete all of the indexes of max_salary from the df.
    employee = employee.drop(indexs_of_max_salary)
    print(employee)
    employee = employee['salary'].max()
    if max_salary == employee: # in case of two employee in the same salary we would send null
        employee = None
    return pd.DataFrame({employee},columns=["SecondHighestSalary"])

ans = second_highest_salary(employee_df)
print(ans)

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    max_salary = employee['salary'].max()
    indexs_of_max_salary = (employee[employee['salary'] == max_salary].index).tolist()
    employee = employee.drop(indexs_of_max_salary)
    employee = employee['salary'].max()
    return pd.DataFrame({employee},columns=["SecondHighestSalary"])