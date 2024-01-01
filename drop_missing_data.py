import pandas as pd

data = [
    {"student_id": 572, "name": "Henry", "age": 8},
    {"student_id": 271, "name": None, "age": 17},
    {"student_id": 315, "name": "Liam", "age": 7},
    {"student_id": 615, "name": "Charlie", "age": 9},
    {"student_id": 564, "name": None, "age": 13}
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

# def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
#     y = 0
#     for i in range(students.shape[1]+1):
#         a = students["name"][i] == None # True
#         if (a):
#             y = i
#     students = students.drop(index=y)
#     return students 


def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    y = 0
    size = students.shape[1]+1
    print('********************************************************')
    for i in range(size):
        print('i', i)
        a = students["name"][i] == None  
        if (a):
            y = i
            students = students.drop(index=y)

    return students



df = createDataframe(data)
# print(df)
ans = dropMissingData(df)
print(ans)