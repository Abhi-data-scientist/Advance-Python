import pandas as pd 
import numpy as np 

mathces = pd.read_csv('IPL_Matches_2008_2022 - IPL_Matches_2008_2022.csv')
print(mathces.head(3))

def teamsApi():
    teams = list(set(list(mathces['Team1']) + list(mathces['Team1'])))
    teams_dict = {
        'teams' : teams
    }    
    return teams_dict