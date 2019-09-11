
n=int(input())
li=[]
for i in range(n):
    ans=0
    a,b,c=list(map(int,input().split(" ")))
    if c==0 and a>b:
        ans=1
    elif c==0 and a<b:
        ans=0
    elif a>b:
        x=a
        a+=c
        while True:
            if a>x and a>b:
                ans+=1
                a-=1
            else :
                break
        ans-=1

    elif a<b and a+c>b:
        x=a
        a+=c
        while True:
            if a>x and a>b:
                ans+=1
                a-=1
            else :
                break
        ans-=1
    else:
        ans=0
    li.append(ans)
for i in range(len(li)):
    print(li[i])
