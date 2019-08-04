n=int(input())

s1=input()
ss1=[]
ss1=s1.split(" ")

s2=input()
ss2=[]
ss2=s2.split(" ")

s3=input()
ss3=[]
ss3=s3.split(" ")
x=list(set(ss1)-set(ss2))
print(x[0])
y=list(set(ss2)-set(ss3))
print(y[0])
