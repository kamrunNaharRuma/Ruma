# How many people who installed the app logged in

from bokeh.plotting import figure,output_file,show, ColumnDataSource
import pandas


df = pandas.read_csv('events.csv')


event_filtered_installed = df[df.type == 'INSTALLED']
event_filtered_loggedin = df[df.type == 'LOGIN_SUCCESS']
installed_filtered_cols = event_filtered_installed[['uid','type']]
loggedin_filtered_cols = event_filtered_loggedin[['uid','type']]

# print (installed_filtered_cols)
# print (loggedin_filtered_cols)

source = ColumnDataSource(installed_filtered_cols)
event_list_installed = set(source.data['uid'].tolist()) 
# 73
# print(event_list_installed)

source = ColumnDataSource(loggedin_filtered_cols)
event_list_loggedIn = set(source.data['uid'].tolist())
# 48
# print(event_list_loggedIn)
dicts = []
#  and uid in dicts is False
for uid in event_list_installed:
    if (uid in event_list_loggedIn) is True:
        dicts.append(uid)

# print(len(dicts))        

number_of_people_installed_loggedIn = {
  "total": len(dicts)
} 

print (number_of_people_installed_loggedIn)