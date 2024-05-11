def f(x):
    return 3*x
print(type(f))
print(f(5))

a = lambda x: 3*x
print(type(a))
print(a(5))

b = lambda f2: sum(f2)
print(b([3, 4, 5]))


