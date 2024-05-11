#prolazak korz listu
arr = ["Sam", "Dave", "Bobby"]
for member in arr:
    print(member)
for i in range(len(arr)):
    print(arr[i], "is on index", i)
print("---------------------")
for k,v in enumerate(arr):
    print(v, "is on index", k)
