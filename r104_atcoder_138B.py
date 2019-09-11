n=int(input())
s=input()
li=s.split()
x=0
for i in range(n):
    x=x+1/int(li[i])
print(1/x)
