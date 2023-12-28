import pandas as pd 
from typing import List
"""


"""
data = [
    {'student_id': 101, 'name': 'Ulysses', 'age': 13},
    {'student_id': 53, 'name': 'William', 'age': 10},
    {'student_id': 128, 'name': 'Henry', 'age': 6},
    {'student_id': 3, 'name': 'Henry', 'age': 11}
]


students = pd.DataFrame(data)

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    print(students)
    # y = [x for x in students]
    row ,column = [students.shape[0],students.shape[1]]
    print(f'row ,column',{row},{column})
    y = [i for i in range(len(row))]
    print('y', y)
    if int(students["student_id"][0]) == 101:
        print("asdfasdfasd asdfasdf  adfasdf  asdfasd ")
    
    # if students["student_id"] == 101:
        # print("this is the right line")
    return None # 
print(selectData(students))