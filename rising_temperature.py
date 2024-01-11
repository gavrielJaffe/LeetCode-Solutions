import pandas as pd

# Define the data
# data = {
#     'id': [1, 2, 3, 4],
#     'recordDate': ['2015-01-01', '2015-01-02', '2015-01-03', '2015-01-04'],
#     'temperature': [10, 25, 20, 30]
# }

# # Create a DataFrame
# weather_df = pd.DataFrame(data)

weather_data = {
    'id': [1, 2],
    'recordDate': ['2000-12-16', '2000-12-15'],
    'temperature': [3, -1]
}

# # Create a DataFrame for Weather
weather_df = pd.DataFrame(weather_data)

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    # sort by Date.
    df = weather.sort_values(by='recordDate',inplace=True)
    df = pd.to_datetime(weather['recordDate'])
    weather = weather.reset_index()
    lst = []
    for i in range(1,weather.shape[0]):
        if(weather['temperature'][i]>weather['temperature'][i-1]):
            lst.append(i)
    return weather.loc[lst][['id']]

ans = rising_temperature(weather_df)
print(ans)