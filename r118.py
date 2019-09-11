def mul(*num):
    print(type(num))
    z=0
    for i in range(len(num)):
        z+=num[i]
    return z
print(mul(1,2,3))

li1=[1,2,3,4,5,6,7,8,9]
a,b,*others=li1
print(a)
print(b)
print(others)