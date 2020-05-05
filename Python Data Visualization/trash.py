# How many people who completed their profile shared their internet or made an internet request.

from bokeh.plotting import figure,output_file,show, ColumnDataSource
import pandas
import json 
import numpy as np

df = pandas.read_csv('events.csv')

# PROFILE_COMPLETED
complete_profile = df[df.type == 'PROFILE_COMPLETED']
complete_profile_filtered_cols = complete_profile[['uid','type']]
# print(complete_profile_filtered_cols)

complete_profile_uid_lst = complete_profile_filtered_cols.uid.unique()
complete_profile_uid = pandas.DataFrame(complete_profile_uid_lst, columns = ['uid']) 
print(complete_profile_uid)

# complete_profile_uid = complete_profile_uid.tolist()
# getting the phone number from LOGGED_SUCCESS list
loggedin = df[df.type == 'LOGIN_SUCCESS']
loggedin_filtered_cols = loggedin[['uid','data']]
print(loggedin_filtered_cols)
# event_list_loggedIn = source.data['uid'].tolist()
# loggedin_filtered_cols.sort_values("uid", inplace = True)

# dicts = []

# for uid in complete_profile_uid:
#     filter = loggedin_filtered_cols["uid"]==uid
#     loggedin_filtered_cols.where(filter, inplace = True)
#     loggedin_filtered_cols['uid'].unique()
#     loggedin_filtered_cols['uid'].dropna().unique()
#     print(loggedin_filtered_cols)
# print(loggedin_filtered_cols)



# source = ColumnDataSource(loggedin_filtered_cols)
# loggedIn_uid = source.data['data'].tolist()




# # importing pandas package 
# import pandas as pd 
  
# # making data frame from csv file 
# data = pd.read_csv("nba.csv") 
  
# # sorting dataframe 
# data.sort_values("Team", inplace = True) 
  
# # making boolean series for a team name 
# filter = data["Team"]=="Atlanta Hawks"
  
# # filtering data 
# data.where(filter, inplace = True) 
  
# # display 
# data 

# source = ColumnDataSource(event_complete_profile)
# data = source.data['data'].tolist()
# data_json= json.loads(data[0])

# print (data_json)

# Shared their internet


