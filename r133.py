n,m=list(map(int,input().split(" ")))
li=list(map(int,input().split(" ")))
li.sort()
num=0
po=0
x=li[0]
for i in range(1,len(li)):
    if li[i]==x:
        num+=1