import decimal
n=int(input())
li=[]
li2=[]
for i in range(n):
    a,b=list(map(float,input().split(" ")))
    '''
    s=input()
    a,b=s.split(" ")
    a=float(a)
    b=float(b)
    '''
    x=int(a)
    print(x)
    x=abs(a)-abs(x)
    print(x)#problem
    y=int(b)
    y=abs(b)-abs(y)
    print(y)
    x=max(len(str(x)),len(str(y)))
    ans=a+b
    li.append(ans)
    li2.append(x)
for i in range(n):
    print(li[i])
    print(li2[i])
    print(round(li[i],li2[i]))

