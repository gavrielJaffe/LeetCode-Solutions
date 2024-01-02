import pandas as pd

data = [
    {"student_id": 1, "name": "Mason", "age": 8},
    {"student_id": 2, "name": "Ava", "age": 6},
    {"student_id": 3, "name": "Taylor", "age": 15},
    {"student_id": 4, "name": "Georgia", "age": 17}
]

data2 = [
    {"student_id": 5, "name": "Leo", "age": 7},
    {"student_id": 6, "name": "Alex", "age": 7}
]

def create_df(data):
    columns_name = ["student_id","name","age"]
    return pd.DataFrame(data,columns=columns_name)

df1 = create_df(data)
df2 = create_df(data2)

# Runtime Beats 7.80% of users with Pandas
def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return pd.concat([df1,df2])    
    
# Beats 23.48% of users with Pandas
def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return df1._append(df2)

    
ans = concatenateTables(df1,df2)
print(ans)
