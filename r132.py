t=int(input())
li=[]
for i in range(t):
    li2=[]
    ans=0
    n,m=list(map(int,input().split(" ")))
    y=m%10
    z=(n//m)+1
    k=1
    for j in range(z):
        if k>10:
            k=1
        ans+=(y*k)%10
            
        
    
    
    li.append(ans)
for i in range(len(li)):
    print(li[i])
