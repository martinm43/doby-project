# coding: utf-8
import pandas as pd
from mlb_database.queries import full_name_to_id
data = pd.read_csv("mlb-2024-AtlanticStandardTime.csv")
data = data.loc[:,['Date','Home Team','Away Team']]
data['Date'] = pd.to_datetime(data['Date'], format='%d/%m/%Y %H:%M')

data['home_team_id']=data['Home Team'].apply(full_name_to_id)

data['home_team_id']=data['Home Team'].apply(full_name_to_id)
data['away_team_id']=data['Away Team'].apply(full_name_to_id)

data['year']=2024

print(data)
