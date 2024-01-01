import pandas as pd 

"""
DataFrame students
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| id          | int    |
| first       | object |
| last        | object |
| age         | int    |
+-------------+--------+

Write a solution to rename the columns as follows:
    id to student_id
    first to first_name
    last to last_name
    age to age_in_years


    Input:
+----+---------+----------+-----+
| id | first   | last     | age |
+----+---------+----------+-----+
| 1  | Mason   | King     | 6   |
| 2  | Ava     | Wright   | 7   |
| 3  | Taylor  | Hall     | 16  |
| 4  | Georgia | Thompson | 18  |
| 5  | Thomas  | Moore    | 10  |
+----+---------+----------+-----+ 
Output:
+------------+------------+-----------+--------------+
| student_id | first_name | last_name | age_in_years |
+------------+------------+-----------+--------------+
| 1          | Mason      | King      | 6            |
| 2          | Ava        | Wright    | 7            |
| 3          | Taylor     | Hall      | 16           |
| 4          | Georgia    | Thompson  | 18           |
| 5          | Thomas     | Moore     | 10           |
+------------+------------+-----------+--------------+
"""
data = [
    {"id": 1, "first": "Mason", "last": "King", "age": 6},
    {"id": 2, "first": "Ava", "last": "Wright", "age": 7},
    {"id": 3, "first": "Taylor", "last": "Hall", "age": 16},
    {"id": 4, "first": "Georgia", "last": "Thompson", "age": 18},
    {"id": 5, "first": "Thomas", "last": "Moore", "age": 10}
]

def createDataframe(data):
    return pd.DataFrame(data,columns=["id","first","last","age"])
students = createDataframe(data)

# Beats 21.17 % of users with Pandas Memory Details 58.69 MB Beats 97.73 % of users with Pandas
def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    return students.rename(columns = {"id":"student_id" ,"first":"first_name" ,"last":"last_name" ,"age":"age_in_years"})

# Beats 46.07 % of users with Pandas , Memory Details 59.43 MB Beats Beats 87.40 % of users with Pandas
def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    students.columns = ["student_id","first_name","last_name","age_in_years"]
    return students

ans = renameColumns(students)
print(ans)
