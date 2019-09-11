def big(a,b,carry=0):
    x=max(len(a),len(b))
    
    ans=[0 for i in range(x)]
    for i in range(x):
        if i<len(a) and i<len(b):
            ans[i]=a[i]+b[i]+carry
            if ans[i]>9:
                carry=ans[i]%10
                ans[i]=ans[i]//10
        elif i>=len(b):
            ans[i]=a[i]+carry
            if ans[i]>9:
                carry=ans[i]%10
                ans[i]=ans[i]//10
        elif i>=len(a):
            ans[i]=b[i]+carry
            if ans[i]>9:
                carry=ans[i]%10
                ans[i]=ans[i]//10
    if carry >0:
        ans.append(carry)
    return ans
def big2(a,b,carry=0):
    x=max(len(a),len(b))
    
    ans=[0 for i in range(x)]
    for i in range(x):
        if i<len(a) and i<len(b):
            ans[i]=a[i]+b[i]+carry
            if ans[i]>9:
                carry=ans[i]%10
                ans[i]=ans[i]//10
        elif i>=len(b):
            ans[i]=a[i]+carry
            if ans[i]>9:
                carry=ans[i]%10
                ans[i]=ans[i]//10
        elif i>=len(a):
            ans[i]=b[i]+carry
            if ans[i]>9:
                carry=ans[i]%10
                ans[i]=ans[i]//10
    
    yield ans
    yield carry
def reverse(string): 
    string = "".join(reversed(string)) 
    return string

a,b=list(map(str,input().split(" ")))
a1,a2=a.split(".")
# print(a1)
# print(a2)

b1,b2=b.split(".")

lia1=list(a1)
lia1=lia1[::-1]
lib1=list(b1)
lib1=lib1[::-1]
lia2=list(a2)
lib2=list(b2)
'''
print(lia1)
print(lib1)
print(lia2)
print(lib2)
'''
x=max(len(lia2),len(lib2))
for i in range(x):
    if i>=len(lia2):
        lia2.append("0")
    if i>=len(lib2):
        lib2.append("0")
# print(lia2)
# print(lib2)
for i in range(len(lia1)):
   lia1[i]=int(lia1[i])
#print(len(lia2))
for i in range(len(lia2)):
    lia2[i]=int(lia2[i])
for i in range(len(lib1)):
    lib1[i]=int(lib1[i])
for i in range(len(lib2)):
    lib2[i]=int(lib2[i])
# print(lia1)
# print(lia2)
# print(lib1)
# print(lib2)
lia2=lia2[::-1]
lib2=lib2[::-1]
an,ca=list(big2(lia2,lib2))
print(an)
print(ca)
ans=big(lia1,lib1,ca)
an=an[::-1]
ans=ans[::-1]
print(str(ans)+"."+str(an))



