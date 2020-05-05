# How many people who shared their internet received a request.
from bokeh.plotting import figure,output_file,show, ColumnDataSource
import pandas
import json 
import numpy as np

# SHARED
df_towerShare = pandas.read_csv('towers.csv')
source = ColumnDataSource(df_towerShare)
towerShare_user_id_list = source.data['user_id'].tolist()
df_towerShare_user_id = pandas.DataFrame(set(towerShare_user_id_list), columns = ['user_id'])
# print(df_towerShare_user_id)


# RECEIVED A REQUEST

df_received_req = pandas.read_csv('shares.csv')
source = ColumnDataSource(df_received_req)
received_req_user_id_list = source.data['host_id'].tolist()
df_received_req_user_id = pandas.DataFrame(set(received_req_user_id_list), columns = ['user_id'])
# print(df_received_req_user_id)
# print(df_received_req_user_id)

# MERGED

merged_user_shared_received = pandas.merge(df_received_req_user_id,df_towerShare_user_id, on = 'user_id')
# print(merged_user_shared_received)
# print(len(merged_user_shared_received.index))

number_of_people_shared_interest_received_request = {
  "total": len(merged_user_shared_received.index)
} 

print(number_of_people_shared_interest_received_request)

