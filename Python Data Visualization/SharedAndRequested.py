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
# print(complete_profile_uid)


loggedin = df[df.type == 'LOGIN_SUCCESS']
loggedin_filtered_cols = loggedin[['uid','data']]
# print(loggedin_filtered_cols)


merged = pandas.merge(complete_profile_uid,loggedin_filtered_cols, on = 'uid')
# print (merged)

source = ColumnDataSource(merged)
event_list_loggedIn = source.data['data'].tolist()
numbers = []
for data in event_list_loggedIn:
    all_data = json.loads(data)
    numbers.append(int(all_data['number'][-9:]))


# print(numbers)
completed_profile_number = pandas.DataFrame(numbers, columns = ['number'])
# print(completed_profile_number)

df_user = pandas.read_csv('users.csv')
user_info = df_user[['_id','number']]
merged_user = pandas.merge(completed_profile_number,user_info, on = 'number')
# print(merged_user)

## CALCULATING THE TOTAL SHARED AND REQUESTED
df_request = pandas.read_csv('requests.csv')
source = ColumnDataSource(df_request)
user_id_list = source.data['user_id'].tolist()
df_user_id = pandas.DataFrame(user_id_list, columns = ['_id'])
merged_user_request = pandas.merge(df_user_id,merged_user, on = '_id')
# print("total request")
# print(len(merged_user_request.index))

df_towers = pandas.read_csv('towers.csv')
source = ColumnDataSource(df_towers)
tower_user_id_list = source.data['user_id'].tolist()
df_tower_user_id = pandas.DataFrame(tower_user_id_list, columns = ['_id'])
merged_user_shared = pandas.merge(df_tower_user_id,merged_user, on = '_id')
# print("total share")
# print(len(merged_user_shared.index))

number_of_people_completed_profile_shared_request = {
  "total_request": len(merged_user_request.index),
  "total_share": len(merged_user_shared.index),
} 

print(number_of_people_completed_profile_shared_request)