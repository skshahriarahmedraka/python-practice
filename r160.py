n=int(input())
li=list(map(int,input().split(' ')))
x=0
ans=0
if li[0]==1:
    j=0
    for i in range(j+1,n):
        if li[i]==1:
            ans+=(i-j)
            j=i
    if ans==0:
        ans+=1
else:
    for i in range(n):
        if li[i]==1:
            j=i
            ans+=1
            break
    for i in range(j+1,n):
        if li[i]==1:
            ans+=(i-j)
            j=i
print(ans)