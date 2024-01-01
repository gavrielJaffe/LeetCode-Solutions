import pandas as pd

data = [
    {"student_id": 572, "name": "Henry", "age": 8},
    {"student_id": 564, "name": None, "age": 13} , 
    {"student_id": 271, "name": None, "age": 17},
    {"student_id": 315, "name": "Liam", "age": 7},
    {"student_id": 615, "name": "Charlie", "age": 9},
    {"student_id": 514, "name": None, "age": 33} , 
    {"student_id": 568, "name": None, "age": 23} , 
    {"student_id": 314, "name": None, "age": 15},
    {"student_id": 981, "name": None, "age": 23},
]

"""
| student_id | name    | age |
| ---------- | ------- | --- |
| 572        | Henry   | 8   |
| 271        | null    | 17  |
| 315        | Liam    | 7   |
| 615        | Charlie | 9   |
| 564        | null    | 13  |
Use Testcase
Output
| student_id | name    | age |
| ---------- | ------- | --- |
| 572        | Henry   | 8   |
| 315        | Liam    | 7   |
| 615        | Charlie | 9   |
| 564        | null    | 13  |
Expected
| student_id | name    | age |
| ---------- | ------- | --- |
| 572        | Henry   | 8   |
| 315        | Liam    | 7   |
| 615        | Charlie | 9   |



"""




def createDataframe(data):
    df = pd.DataFrame(data,columns = ["student_id","name","age"])
    return df

# Beats 69.60 % of users with Pandas
def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    size = students.shape[0]
    i = 0
    while (i < size):
        if (students["name"][i] == None ):
            students = students.drop(index=i)
        i+=1
    return students

# Beats 63.75 % of users with Pandas
def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    students.dropna(subset=['name'], inplace=True)
    return students

# Beats 79.51 % of users with Pandas
def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame(students)[students['name'].notnull()]

#Best way - Beats 86.48 % of users with Pandas
def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame(students)[students['name'].notna()]

df = createDataframe(data)
# print(df)
ans = dropMissingData(df)
print(ans)