import marshal

string_pre="ITA"
print(string_pre)

o=marshal.dumps(string_pre)
print(o)

string_posle=marshal.loads(o)
print(string_posle)