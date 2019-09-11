t=int(input())
li2=[]
for i in range(t):
    n=int(input())
    ans=0
    li=list(map(int,input().split()))
    if n==1:
        li2.append(0)
        continue
    if n==0:
        li2.append(0)
        continue
    for j in range(0,len(li)-1):
        for k in range(j+1,len(li),1):
            if li[k]<li[j]:
                ans+=1
                break
    li2.append(ans)

for i in range(len(li2)):
    print(li2[i])