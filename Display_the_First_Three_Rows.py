# Display the First Three Rows
import pandas as pd 
from typing import List

data = [
    {
        "employee_id": 3,
        "name": "Bob",
        "department": "Operations",
        "salary": 48675
    },
    {
        "employee_id": 90,
        "name": "Alice",
        "department": "Sales",
        "salary": 11096
    },
    {
        "employee_id": 9,
        "name": "Tatiana",
        "department": "Engineering",
        "salary": 33805
    },
    {
        "employee_id": 60,
        "name": "Annabelle",
        "department": "InformationTechnology",
        "salary": 37678
    },
    {
        "employee_id": 49,
        "name": "Jonathan",
        "department": "HumanResources",
        "salary": 23793
    },
    {
        "employee_id": 43,
        "name": "Khaled",
        "department": "Administration",
        "salary": 40454
    }
]

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame(employees)
    return df.iloc[:3] # Only the first 3 rows are displayed.

# Best way to get the first 3 rows
def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame(employees)
    return df.head(3) # Only the first 3 rows are displayed.

print(selectFirstRows(data))