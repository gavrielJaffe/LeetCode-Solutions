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

# Beats 89.99 % of users with Pandas
def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    # Find all of the indexes of the max_salary in the df.
    max_salary = employee['salary'].max()
    indexs_of_max_salary = (employee[employee['salary'] == max_salary].index).tolist()
    # Drop rows with indices stored in indices_of_max_salary from the DataFrame
    employee = employee.drop(indexs_of_max_salary)
    employee = employee['salary'].max() # second highest max
    return pd.DataFrame({employee},columns=["SecondHighestSalary"])

ans = second_highest_salary(employee_df)
print(ans)

# Beats 70.97%of users with Pandas
def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    max_salary = employee['salary'].max()
    indexs_of_max_salary = (employee[employee['salary'] == max_salary].index).tolist()
    employee = employee.drop(indexs_of_max_salary)
    employee = employee['salary'].max()
    return pd.DataFrame({employee},columns=["SecondHighestSalary"])