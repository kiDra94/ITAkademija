x = 1
def f():
    x = 2 #localna samo se u funkciji vidi
    print(x)
f()
print(x) # globalni; van je funkcije i ona ga ne vidi
print("----------------------")
x = 1
def f():
    global x
    x = 2 #localna samo se u funkciji vidi
    print(x)
f()
print(x) # stampa 2 zato sto je x global
print("----------------------")