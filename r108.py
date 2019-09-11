def po(a,b):
    x=1
    for i in range(b):
        x=x*a
    return x

n,k=input().split(" ")
n=int(n)
k=int(k)
s=input()
li=s.split(" ")


ans=1
for i in range(len(li)-1):
    if li[i]!=li[i+1]:
        ans+=1
print(po(ans,k)-1)