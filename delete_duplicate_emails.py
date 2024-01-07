import pandas as  pd 

data = {
    'id': [1, 2, 3],
    'email': ['john@example.com', 'bob@example.com', 'john@example.com']
}

data1 = [
    {"id": 2, "email": "abc@efg.com"},
    {"id": 1, "email": "abc@efg.com"}
]
# Output :  We keep the row with the smallest Id = 1.


person = pd.DataFrame(data1)
# works
def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.sort_values('id',inplace=True)
    person.drop_duplicates('email',inplace=True)
    return 

ans = delete_duplicate_emails(person)
print(person)