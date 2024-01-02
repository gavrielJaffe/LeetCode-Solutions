"""
Input:
+--------------+----------+-------------+
| city         | month    | temperature |
+--------------+----------+-------------+
| Jacksonville | January  | 13          |
| Jacksonville | February | 23          |
| Jacksonville | March    | 38          |
| Jacksonville | April    | 5           |
| Jacksonville | May      | 34          |
| ElPaso       | January  | 20          |
| ElPaso       | February | 6           |
| ElPaso       | March    | 26          |
| ElPaso       | April    | 2           |
| ElPaso       | May      | 43          |
+--------------+----------+-------------+
Output:
+----------+--------+--------------+
| month    | ElPaso | Jacksonville |
+----------+--------+--------------+
| April    | 2      | 5            |
| February | 6      | 23           |
| January  | 20     | 13           |
| March    | 26     | 38           |
| May      | 43     | 34           |
+----------+--------+--------------+

"""
import pandas as pd 

data =[ 
    {"city": "Jacksonville", "month": "January", "temperature": 13},   
    {"city": "Jacksonville", "month": "February", "temperature": 23}, 
    {"city": "Jacksonville", "month": "March", "temperature": 38},   
    {"city": "Jacksonville", "month": "April", "temperature": 5}, 
    {"city": "Jacksonville", "month": "May", "temperature": 34}, 
    {"city": "ElPaso", "month": "January", "temperature": 20},  
    {"city": "ElPaso", "month": "February", "temperature": 6},  
    {"city": "ElPaso", "month": "March", "temperature": 26},
    {"city": "ElPaso", "month": "April", "temperature": 2},   
    {"city": "ElPaso", "month": "May", "temperature": 43}
    ]

weather = pd.DataFrame(data,columns=["city","month","temperature"])

# Beats 97.78%of users with Pandas
def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    return weather.pivot(index='month', columns='city', values='temperature')    

# def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
#     return weather.pivot_table(values='temperature', index='month', columns = 'city',aggfunc='max')
ans  = pivotTable(weather)
print(ans)

