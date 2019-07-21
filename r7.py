n=int(input())
k=int(input())
t=0
p=0
q=0
r=0
s=0
li=[]
i=0
while i<n:
    li.insert(i,int(input()))
    i=i+1
i=0
while i<(n-k):
    q=i
    p=0
    j=0
    while j<k:
        p=p+li[q]
        
        q=q+1
        j=j+1
    
    if t==0:
        r=p
        t=1
    if p<r :
      
        r=p
        s=q-k
    i=i+1

print(s+1)
