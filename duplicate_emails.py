"""
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| email       | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table contains an email. The emails will not contain uppercase letters.

 

Write a solution to report all the duplicate emails. Note that it's guaranteed that the email field is not NULL.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Person table:
+----+---------+
| id | email   |
+----+---------+
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com |
+----+---------+
Output: 
+---------+
| Email   |
+---------+
| a@b.com |
+---------+

"""
import pandas as pd

data = [
    {"id": 1, "email": "a@b.com"},
    {"id": 2, "email": "c@d.com"},
    {"id": 3, "email": "a@b.com"}
]

data2 = {
    'id': [1, 2, 3],
    'email': ['jacky@yahoo.com', 'jacky@yahoo.com', 'jacky@yahoo.com']
}
df = pd.DataFrame(data2)

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    return person.loc[person[person['email'].duplicated()].index][["email"]].drop_duplicates()


ans = duplicate_emails(df)
print(ans)