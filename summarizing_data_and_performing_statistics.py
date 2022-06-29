"""
You need to crunch through large datasets and generate summaries or other kinds of
statistics.
The data is here https://data.cityofchicago.org/Service-Requests/311-Service-Requests-Rodent-Baiting-Historical/97t6-zrhs
"""
import pandas

# Read a CSV file, skipping last line
rats = pandas.read_csv('rats.csv', skip_footer=1)

# Investigate range of values for a certain field
rats['Current Activity'].unique()
# array([nan, Dispatch Crew, Request Sanitation Inspector], dtype=object)

# Filter the data
crew_dispatched = rats[rats['Current Activity'] == 'Dispatch Crew']

# Find 10 most rat-infested ZIP codes in Chicago
crew_dispatched['ZIP Code'].value_counts()[:10]
len(crew_dispatched)

# Group by completion date
dates = crew_dispatched.groupby('Completion Date')
# <pandas.core.groupby.DataFrameGroupBy object at 0x10d0a2a10>

# Determine counts on each day
date_counts = dates.size()

# Sort the counts
date_counts.sort()
