n=int(input())
s=input()
li=s.split(" ")
for i in range(len(li)):
    li[i]=int(li[i])
li.sort()
ans=(li[0]+li[1])/2
if len(li)>2:
    for i in range(2,len(li)):
        ans=(ans+li[i])/2
print(ans)