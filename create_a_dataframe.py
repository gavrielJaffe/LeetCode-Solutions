import pandas as pd
from typing import List

student_data = [
  [1, 15],
  [2, 11],
  [3, 11],
  [4, 20],
]

def createDataframe(student_data):
    df = pd.DataFrame({"student_id":[x[0] for x in student_data] , "age":[x[1] for x in student_data]})
    return df
    
# Best way to build a df . 
def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    colume_name = ["student_id", "age"]
    df = pd.DataFrame(student_data,columns=colume_name)
    return df

print(createDataframe(student_data))
