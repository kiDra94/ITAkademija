import requests
import json

# Now we have to request our JSON data through
# the API package
res = requests.get("https://jsonplaceholder.typicode.com/todos")
users = json.loads(res.text)

# To view your Json data, type var and hit enter
print(users)