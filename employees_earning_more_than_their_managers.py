import pandas as pd 

"""
Input: 
Employee table:
+----+-------+--------+-----------+
| id | name  | salary | managerId |
+----+-------+--------+-----------+
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | Null      |
| 4  | Max   | 90000  | Null      |
+----+-------+--------+-----------+
Output: 
+----------+
| Employee |
+----------+
| Joe      |
+----------+

"""
data = [
    {
        "id": 1,
        "name": "Joe",
        "salary": 70000,
        "managerId": 3
    },
    {
        "id": 2,
        "name": "Henry",
        "salary": 80000,
        "managerId": 4
    },
    {
        "id": 3,
        "name": "Sam",
        "salary": 60000,
        "managerId": "null"
    },
    {
        "id": 4,
        "name": "Max",
        "salary": 90000,
        "managerId": "null"
    }
]

data1 = [
    {
        "id": 1,
        "name": "Mark",
        "salary": 40000,
        "managerId": 2
    },
    {
        "id": 3,
        "name": "Jack",
        "salary": 30000,
        "managerId": 2
    },
    {
        "id": 2,
        "name": "Alan",
        "salary": 20000,
        "managerId": "null"
    }
]

df = pd.DataFrame(data1)

# works for data ,not for data1 
def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    d = {'Employee': []}
    df4 = pd.DataFrame(data=d)   
    for i in range(employee.shape[0]): # bug here
        if (isinstance(employee['managerId'].iloc[i], int)):
            pos = (employee['managerId'].iloc[i])
            if ((employee['salary'].iloc[i]) > (employee.loc[employee['id'][pos],'salary'])):
                username = employee['name'][i] # Mark ,Jack
                # Apeend to df4 
                new_row = {'Employee': username}
                df4.loc[len(df4)] = new_row
    return df4

# with gpt
def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    df4 = pd.DataFrame(columns=['Employee'])  # Create an empty DataFrame with column 'Employee'
    
    for i in range(employee.shape[0]):
        manager_id = employee['managerId'].iloc[i]
        if manager_id != 'null' and pd.notnull(manager_id):
            manager_id = int(manager_id)
            if employee['salary'].iloc[i] > employee.loc[employee['id'] == manager_id, 'salary'].values:
                username = employee['name'].iloc[i]  # Get the employee's name
                df4 = df4._append({'Employee': username}, ignore_index=True)  # Append to df4
    
    return df4


ans = find_employees(df)
print(ans)






# works for data1,
# def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
#     d = {'Employee': []}
#     df4 = pd.DataFrame(data=d)   
#     for i in range(employee.shape[0]):
#         if (isinstance(employee['managerId'].iloc[i], int)):
#             pos = (employee['managerId'].iloc[i])
            
#             # print(employee.loc[employee['id'][pos],'salary']) # 20,000
#             if ((employee['salary'].iloc[i]) > (employee.loc[employee['id'][pos],'salary'])):
#                 # print(employee['name'][i]) # Mark ,Jack
#                 username = employee['name'][i] # Mark ,Jack
#                 # Apeend to df4 
#                 new_row = {'Employee': username}
#                 df4.loc[len(df4)] = new_row
#                 # print(df4)
#     return df4

# def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    # df1 = employee['managerId'].to_frame()
    # df2 = employee['id'].to_frame().rename(columns={"id":"managerId"})
    # mng_df = df1.merge(df2)
    # wrk_df = employee.merge(mng_df)
    # df2 = mng_df['managerId'].to_frame().rename(columns={"managerId":"id"})
    # manger_sal_df = employee.merge(df2)
    # wrk_df = wrk_df[wrk_df['salary'] > manger_sal_df['salary']]
    # rest = pd.DataFrame(wrk_df['name']).rename(columns={"name":"Employee"})
    # return rest