import pandas as pd 

data = [
    {"customer_id": 1, "name": "Ella", "email": "emily@example.com"},
    {"customer_id": 2, "name": "David", "email": "michael@example.com"},
    {"customer_id": 3, "name": "Zachary", "email": "sarah@example.com"},
    {"customer_id": 4, "name": "Alice", "email": "john@example.com"},
    {"customer_id": 5, "name": "Finn", "email": "john@example.com"},
    {"customer_id": 6, "name": "Violet", "email": "alice@example.com"},
]

def createdf(data):
    columns_names = ["customer_id","name","email"]
    df = pd.DataFrame(data, columns = columns_names)
    return df 
customers = createdf(data)

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates(subset=["email"])

# Beats 63.71% of users with Pandas
def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates(subset="email",keep='first')

ans = dropDuplicateEmails(customers)
print(ans)