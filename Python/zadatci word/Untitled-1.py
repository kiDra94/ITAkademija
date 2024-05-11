def alfa(string):
    for i in string:
        if i.isalpha():
            yield i
string = input("Unesi string koji sadrzi brojeve i karaktere: ")
for j in alfa(string):
    print(j, end=" ")
