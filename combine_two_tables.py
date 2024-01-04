import pandas as pd 
# 175. Combine Two Tables
person_data = {
    'personId': [1, 2],
    'lastName': ['Wang', 'Alice'],
    'firstName': ['Allen', 'Bob']
}
person = pd.DataFrame(person_data)
# Creating the Address DataFrame
address_data = {
    'addressId': [1, 2],
    'personId': [2, 3],
    'city': ['New York City', 'Leetcode'],
    'state': ['New York', 'California']
}
address = pd.DataFrame(address_data)

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    return person.merge(address ,on="personId",how="left")[["firstName","lastName","city","state"]]

ans = combine_two_tables(person, address)
# print(ans)