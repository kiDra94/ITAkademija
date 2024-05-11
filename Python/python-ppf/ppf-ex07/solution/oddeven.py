a = [3,7,1,9,2,4,5,12]
odd = []
even = []
for num in a:
    even.append(num) if num % 2 == 0 else odd.append(num)
print("Odds:")
print(odd)
print("Evens:")
print(even)