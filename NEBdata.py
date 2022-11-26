from __future__ import print_function
import cfbd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
import requests
import time
from cfbd.rest import ApiException
from pprint import pprint

configuration = cfbd.Configuration()
configuration.api_key['Authorization'] = 'R8yFjf+V8RcIeRMyzwsSoNY4TbzZAEGl4/Z22KZwzgmEDU0a7STcOEAMVOs3pYjf'
configuration.api_key_prefix['Authorization'] = 'Bearer'
api_config = cfbd.ApiClient(configuration)

api_instance = cfbd.BettingApi(cfbd.ApiClient(configuration))
season_type = 'regular'
# List of teams and has a ton of info

# Highlight and unhighlight Shft + Alt + A
""" teams_api = cfbd.TeamsApi(api_config)
teams_api.get_fbs_teams()
teamname = teams_api.get_fbs_teams()
print(teamname) """



def drives():
    year = 2022 # int | Year Filter
    week = 7 # int | Week filter (optional)
    team = 'Nebraska' # str | Team filter (optional)


    api_instance = cfbd.DrivesApi(cfbd.ApiClient(configuration))
    unformatted_result_list = api_instance.get_drives(season_type=season_type, year=year, week=week,team=team)

    print('-------------------------------------------------------------------------------------')
    fullgamedrives(unformatted_result_list)
    #print(formatted)

def fullgamedrives(unformatted_result_list):    
    df = pd.DataFrame.from_records([dict(offense=d.offense, scoring=d.scoring, start_period=d.start_period, start_yardline=d.start_yardline, start_yards_to_goal=d.start_yards_to_goal, plays=d.plays, yards=d.yards, drive_result=d.drive_result, end_offense_score = d.end_offense_score, end_defense_score=d.end_defense_score ) for d in unformatted_result_list])
    neb = 'Nebraska'
    datatable = df
    print (datatable)
    

drives()

