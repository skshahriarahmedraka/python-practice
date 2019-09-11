def func(n):
    yield 1
    print("what 1")
    
    yield 2
    print("whats 2")
    return 5
    yield 3
    print("whats 3")
    if n>0:
        func(n-1)
        yield n
    
    
def getfac(n):
    yield 23
    if n<2:
        return 1
    else :
        return n*getfac(n-1)

z=list(func(3))
print(z)
''''
zz=int(float("12.23"))
print(zz)
li=[123]


r=list(getfac(5))
print(r)
'''