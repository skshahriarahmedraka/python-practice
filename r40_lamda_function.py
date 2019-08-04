def func(n):
    return lambda a: a*n 

x=func(12)
print(x(12))