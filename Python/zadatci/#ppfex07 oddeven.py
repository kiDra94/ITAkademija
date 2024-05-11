#ppfex07 oddeven
a    = [3,7,1,9,2,4,5,12]
odd  = []
even = []
for i in a:
    even.append(i) if i%2==0 else odd.append(i)
print(odd)
print(even)