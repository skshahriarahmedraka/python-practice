def func1(b):
    if( b%2 == 0):
        b=b//2
        print(b)
        return b
    else :
        b=3*b+1
        print(b)
        return b

a=int(input())
while True:
    a=func1(a)
    if(a==1):
        break


