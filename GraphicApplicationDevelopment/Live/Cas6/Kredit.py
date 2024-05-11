glavnica = int(input("Unesi glavnicu: "))
procenat = int(input("Unesi procenat: "))
vrijeme = int(input("Unesi vrijeme u godinama: "))

def kredit(glavnica, procenat, vrijeme):
    return  round(glavnica*(pow((1+(procenat/100)), vrijeme)))

print(kredit(glavnica, procenat, vrijeme))