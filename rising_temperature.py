import pandas as pd

# Define the data
data = {
    'id': [1, 2, 3, 4],
    'recordDate': ['2015-01-01', '2015-01-02', '2015-01-03', '2015-01-04'],
    'temperature': [10, 25, 20, 30]
}

# Create a DataFrame
weather_df = pd.DataFrame(data)

# Display the DataFrame
print(weather_df)
