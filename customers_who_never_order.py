import pandas as pd 

customers_data = {
    "id": [1, 2, 3, 4],
    "name": ['Joe', 'Henry', 'Sam', 'Max']
}

orders_data = {
    "id": [1, 2],
    "customerId": [3, 1]
}



customers_data1 = {
    "id": [1],
    "name": ['Sam']
}

orders_data1 = {
    "id": [],
    "customerId": []
}
# Expected  : | Customers 
#             |    Sam   |



customers_data3 = {
    "id": [],
    "name": []
}

orders_data3 = {
    "id": [],
    "customerId": []
} # Expected  : | Customers 
  #             | --------- |

customers = pd.DataFrame(customers_data3)
orders = pd.DataFrame(orders_data3)

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # print(customers)
    df = ((customers.loc[orders['customerId']].sort_index())[['name']].rename(columns = {"name":"Customers"})) # Hennry, Max by name 
    
    
    if df.empty:
        print("from the empy df ")
        if not customers.empty and orders.empty:
            return customers.rename(columns = {"name":"Customers"})
    

    return df

# def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
#     return  (customers.loc[orders['customerId']].sort_index())[['name']].rename(columns = {"name":"Customers"})
    # customers = customers.rename(columns = {"name":"Customers"})
    # print((customers.loc[orders['customerId']].sort_index())[['name']]) # Hennry, Max by name 




ans = find_customers(customers, orders)
print(ans)