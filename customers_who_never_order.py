import pandas as pd 

# customers_data3 = {
#     "id": [],
#     "name": []
# }

# orders_data3 = {
#     "id": [],
#     "customerId": []
# } # Expected  : | Customers 
#   #             | --------- |


customers_data1 = {
    "id": [1],
    "name": ['Sam']
}

orders_data1 = {
    "id": [1],
    "customerId": [1]
}
# Expected  : | Customers 
#             |    Sam   |


customers_data = {
    "id": [1, 2, 3, 4],
    "name": ['Joe', 'Henry', 'Sam', 'Max']
}

orders_data = {
    "id": [1, 2],
    "customerId": [3, 1]
}


customers = pd.DataFrame(customers_data)
orders = pd.DataFrame(orders_data)


def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    ctmr_who_never_order = orders["customerId"].tolist()
    ctmr_ids= customers["id"].tolist()
    ctmr_ids = [x for x in ctmr_ids if x not in ctmr_who_never_order]
    print(ctmr_ids)
    filtered_customers = customers[customers['id'].isin((ctmr_ids))]
    filtered_customers= filtered_customers.rename(columns = {"name":"Customers"})
    return filtered_customers[['Customers']]


ans = find_customers(customers, orders)
print(ans)




















# def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
#     # print(customers.loc[orders['customerId']])
#     try:
#         df = (customers.loc[orders['customerId']].sort_index())[['name']]
#         df = df.rename(columns = {"name":"Customers"})
#         if df.empty:
#             # print("it empty df")
#             if customers.empty and orders.empty:
#                 return df[['Customers']]
#             if customers.empty and not orders.empty:
#                 # print("40")
#                 customers = customers.rename(columns = {"name":"Customers"})
#                 return customers[['Customers']]
#         if not customers.empty and orders.empty:    
#             customers = customers.rename(columns = {"name":"Customers"})
#             return customers[['Customers']]
#         return df 
#     except KeyError as e :
#         customers = customers.rename(columns = {"name":"Customers"})
#         indexs_of = (customers['Customers'].index).tolist()
#         # x = (customers[customers['Customers'] == orders["customerId"]].index).tolist()
#         # print(orders[['id']])

#         # print(indexs_of)
#         print('********************************************************')
#         return customers[['Customers']]
        



# customers_data = {
#     "id": [1, 2, 3, 4],
#     "name": ['Joe', 'Henry', 'Sam', 'Max']
# }

# orders_data = {
#     "id": [1, 2],
#     "customerId": [3, 1]
# }










