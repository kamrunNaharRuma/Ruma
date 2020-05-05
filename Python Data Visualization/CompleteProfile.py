# How many people who logged in completed their profile
from bokeh.plotting import figure,output_file,show, ColumnDataSource
import pandas


df = pandas.read_csv('events.csv')

# PROFILE_COMPLETED
complete_profile = df[df.type == 'PROFILE_COMPLETED']
complete_profile_filtered_cols = complete_profile[['uid','type']]

# print(complete_profile_filtered_cols)
df_complete_profile_unique= complete_profile_filtered_cols.drop_duplicates()
total_completed_profile= len(df_complete_profile_unique.index)
# total_profile= event_complete_profile['type'].value_counts().tolist()

number_of_people_completed_profile = {
  "total": total_completed_profile
} 

print(number_of_people_completed_profile)