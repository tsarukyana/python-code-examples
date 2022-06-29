"""
You want to read or write data encoded as JSON (JavaScript Object Notation).
"""
import json

data = {
    'name': 'ACME',
    'shares': 100,
    'price': 542.23
}
json_str = json.dumps(data)

# Here is how you turn a JSON-encoded string back into a Python data structure:
data = json.loads(json_str)

# Writing JSON data
with open('data.json', 'w') as f:
    json.dump(data, f)
# Reading data back
with open('data.json', 'r') as f:
    data = json.load(f)
