with open("izrazi.txt", "r") as f:
   lines = f.readlines()
with open("izlaz.txt", "w") as f2:
    for l in lines:
        if l[1] == "+":
            f2.write(f"{l[0]}+{l[2]}={int(l[0]) + int(l[2])}\n")
        else:
            f2.write(f"{l[0]}-{l[2]}={int(l[0]) - int(l[2])}\n")
