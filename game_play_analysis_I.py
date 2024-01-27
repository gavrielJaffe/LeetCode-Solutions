import pandas as pd 
import csv
activity_data = {
    "player_id":[1,1,2,3,3,1],
    "device_id":[2,2,3,1,4,1],
    "event_date":["2016-03-01","2016-05-02","2017-06-25","2016-03-02","2018-07-03","2015-01-01"],
    "games_played":[5,6,1,0,5,1],
}

# df = pd.DataFrame()
df_activity = pd.DataFrame(activity_data)

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity = activity.groupby('player_id')['event_date'].min().reset_index()
    activity = activity.rename(columns = {"event_date":"first_login"})
    return activity [["player_id","first_login"]]


ans = game_analysis(df_activity)
print(ans)



# Output : 
#  player_id | first_login |
# | --------- | ----------- |
# | 1         | 2019-01-13  | <-
# | 2         | 2019-02-22  | <-
# | 3         | 2019-02-02  | <-
# | 4         | 2019-01-05  |
# | 5         | 2019-03-20  |
# | 6         | 2019-01-16  |...


# Expected
# Open Raw
# | player_id | first_login |
# | --------- | ----------- |
# | 1         | 2019-01-01  |  <-
# | 2         | 2019-01-04  |  <-
# | 3         | 2019-01-13  |  <-
# | 4         | 2019-01-04  |
# | 5         | 2019-01-12  |
# | 6         | 2019-01-14  |...

# still have the log ...  