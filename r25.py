import math

n=input()
b=True
li=[]
for x in range(n):
    a,b=input().split(" ")
    a=float(a)
    b=float(b)
    if((len(str(a))-len(str(math.trunc(a)))) >= (len(str(b))-len(str(math.trunc(b)))))
        li[x]=round(float(a)+float(b),len(str(a))-len(str(math.trunc(a)))-1)
    elif((len(str(a))-len(str(math.trunc(a))))<len(str(b))-len(str(math.trunc(b))))
        li[x]=round(float(a)+float(b),len(str(b))-len(str(math.trunc(b)))-1)
for x in range(n):
    print(li[x])