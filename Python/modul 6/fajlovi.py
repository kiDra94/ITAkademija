with open("Assigment_manipulacija_nad_fajlom\izrazi.txt", "r") as f:
   lines = f.readlines()
with open("123.2.txt", "w") as f2:
    for l in lines:
        if l[1] == "+":
            a = int(l[0])
            b = int(l[2])
            c = a + b
            f2.write(f"\n{a}+{b}={c}")
        else:
            a = int(l[0])
            b = int(l[2])
            c = a - b
            f2.write(f"\n{a}-{b}={c}")
with open("123.2.txt", "r") as f3:
    print(f3.read())