# How many people who received a request accepted or rejected the request.
from bokeh.plotting import figure,output_file,show, ColumnDataSource
import pandas
import json 
import numpy as np

# RECEIVED A REQUEST

    # df_received_req = pandas.read_csv('shares.csv')
    # source = ColumnDataSource(df_received_req)
    # received_req_user_id_list = source.data['host_id'].tolist()
    # df_received_req_user_id = pandas.DataFrame(set(received_req_user_id_list), columns = ['user_id'])
    # print(df_received_req_user_id)

#ACCEPTED THE REQUEST
df = pandas.read_csv('shares.csv')
status_approved = df[df.status == 'approved']
# print(len(status_approved.index))
#REJECTED THE REQUEST

status_rejected = df[df.status == 'rejected']
# print(len(status_rejected.index))

total_accepts_rejects = {
  "total_accepts": len(status_approved.index),
  "total_rejects": len(status_rejected.index),
} 

print(total_accepts_rejects)