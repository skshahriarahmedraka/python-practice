s=input()
n=int(input())
li=[]
def string(s,i,x):
    return s[i*x:(i+1)*x]

for i in range(int(len(s)/n)):
    li.append(list(string(s,i,n)))
#print(li)
x=n
for i in range(int(len(s)/n)):
    for j in range(int(len(li[i])/2)+1):
        for k in range(j,len(li[i])):
            if j!=k and li[i][j]==li[i][k]:
                del li[i][k]
                break
for i in range(int(len(s)/n)):
    for j in range(len(li[i])):
        print(li[i][j],end="")     
    print(end="\n")   


