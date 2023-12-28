# 2878. Get the Size of a DataFrame 
"""
DataFrame players:
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| player_id   | int    |
| name        | object |
| age         | int    |
| position    | object |
| ...         | ...    |
+-------------+--------+

write a solution to calculate and display the number of rows and columns of players.

Return the result as an array:

[number of rows, number of columns]

The result format is in the following example
"""
import pandas as pd 
from typing import List
data_player = [
    {
        "player_id": 71,
        "name": "Alice",
        "age": 21,
        "position": "Winger",
        "team": "RealMadrid"
    },
    {
        "player_id": 35,
        "name": "Ava",
        "age": 25,
        "position": "Sweeper",
        "team": "Barcelona"
    },
    {
        "player_id": 202,
        "name": "Mason",
        "age": 15,
        "position": "Sweeper",
        "team": "ManchesterUnited"
    },
    {
        "player_id": 688,
        "name": "Emily",
        "age": 35,
        "position": "Sweeper",
        "team": "Liverpool"
    },
    {
        "player_id": 311,
        "name": "Kate",
        "age": 17,
        "position": "Center-back",
        "team": "BayernMunich"
    },
    {
        "player_id": 992,
        "name": "Kai",
        "age": 40,
        "position": "Midfielder",
        "team": "Chelsea"
    },
    {
        "player_id": 128,
        "name": "Uma",
        "age": 26,
        "position": "Striker",
        "team": "Juventus"
    },
    {
        "player_id": 5,
        "name": "Isabella",
        "age": 31,
        "position": "Striker",
        "team": "ParisSaint-Germain"
    },
    {
        "player_id": 348,
        "name": "Ulysses",
        "age": 20,
        "position": "Striker",
        "team": "ManchesterCity"
    },
    {
        "player_id": 412,
        "name": "Georgia",
        "age": 19,
        "position": "Fullback",
        "team": "Arsenal"
    },
    {
        "player_id": 821,
        "name": "Liam",
        "age": 33,
        "position": "Center-back",
        "team": "RealMadrid"
    }
]

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    colume_name = ["player_id", "name","age","position","team"]
    df = pd.DataFrame(players,columns=colume_name)
    return [len(df),len(df.columns)] # [number of rows, number of columns]

# Best way - Beats 76.57%
def getDataframeSize(players: pd.DataFrame) -> List[int]:
    colume_name = ["player_id", "name","age","position","team"]
    df = pd.DataFrame(players,columns=colume_name)
    return [df.shape[0],df.shape[1]] # [number of rows, number of columns]

print(getDataframeSize(data_player))