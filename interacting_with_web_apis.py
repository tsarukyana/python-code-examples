"""
Many websites have public APIs providing data feeds via JSON or some
other format. There are a number of ways to access these APIs from
Python; one method that I recommend is the requests package.

To find the last 30 GitHub issues for pandas on GitHub, we can make a
GET HTTP request using the add-on requests library:
"""
import requests
import pandas as pd

url = 'https://api.github.com/repos/pandas-dev/pandas/issues'

resp = requests.get(url)

data = resp.json()
print(data[0]['title'])

issues = pd.DataFrame(data, columns=['number', 'title', 'labels', 'state'])

print(issues)
