m,d=input().split(" ")
m=int(m)
d=int(d)
ans=0
for i in range(m):
    for j in range(d):
        if len(str(j+1))>=2:
            k=j+1
            k=str(k)
            if int(k[0])>=2 and int(k[1])>=2 and (i+1)==(int(k[0])*int(k[1])):
                ans+=1
print(ans)