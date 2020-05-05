# How many people installed the app in distinct locations

from bokeh.plotting import figure,output_file,show, ColumnDataSource
import pandas
import json 
import numpy as np

# EVENTS TYPE = SHARE_SCAN_LOCATION
df = pandas.read_csv('events.csv')
location = df[df.type == 'SHARE_SCAN_LOCATION']
location_cols = location[['uid','data']]
source = ColumnDataSource(location_cols)
location_list = source.data['data'].tolist()
locations = []
for data in location_list:
    location = json.loads(data)
    locations.append({location['latitude'],location['longitude']})

df_locations = pandas.DataFrame(locations, columns = ['latitude','longitude'])

print(df_locations)

df_location_unique= df_locations.drop_duplicates()
print (len(df_location_unique.index))

app_installed_in_distinct_location = {
  "total_distinct_location": len(df_location_unique.index)
} 

print(app_installed_in_distinct_location)