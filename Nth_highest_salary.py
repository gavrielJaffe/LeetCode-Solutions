


import pandas as pd

data = {
    'id': [1,2,3],
    'salary': [100,200,300]
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

data6 = [
    {"id": 1, "salary": 100},
    {"id": 2, "salary": 200},
    {"id": 3, "salary": 300}
]


employee_df = pd.DataFrame(data6)

def nth_highest_salary(employee: pd.DataFrame , N :int) -> pd.DataFrame:
    for i in range(N-1):
        max_salary = employee['salary'].max()
        # Find all of the indexes of the max_salary in the df.
        indexs_of_max_salary = (employee[employee['salary'] == max_salary].index).tolist()
        # Drop rows with indices stored in indices_of_max_salary from the DataFrame
        employee = employee.drop(indexs_of_max_salary)

    if N >= 0:
        employee = employee['salary'].max() # last highest max salary
        return pd.DataFrame({employee},columns=[f"getNthHighestSalary({(N)})"])
    elif N <= 0:
        return pd.DataFrame({f"getNthHighestSalary({(N)})": ["null"]})


ans = nth_highest_salary(employee_df,-1)
print('ans', ans)

