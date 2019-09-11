n=input()
s=input()
ans=0
for i in range(len(n)):
    if s[i]==n[i]:
        ans+=1
print(ans)