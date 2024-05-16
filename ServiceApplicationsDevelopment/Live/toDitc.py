import json

# JSON string
employee = '{"id":"09", "name": "Nitin", "department":"Finance"}'
print("This is JSON", type(employee))

print("\nNow convert from JSON to Python")

# Convert string to Python dict
employee_dict = json.loads(employee) #json.laods pretvara str u dict
print("Converted to Python", type(employee_dict)) 
print(employee_dict)