def sqrt(value):
    if not isinstance(value,(int,float)):
        raise TypeError("values must be numaric")
    elif value<0:
        raise ValueError("value must be non negetive ")

#n=float(input())
#n=int(input())
n=input()
sqrt(n)