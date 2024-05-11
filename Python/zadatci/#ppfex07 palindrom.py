#ppfex07 palindrom
s = str(input("Unesite rijec: "))
s = s.lower()
print(s, "Jeste palindrom" if s[::-1] == s[::] else "Nije palindrom")
