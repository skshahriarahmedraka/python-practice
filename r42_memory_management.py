x=10
print(type(x))
y=x
if(id(x)==id(y)):
    print("x and y are in same address")
x=12
if(id(x)==id(y)):
    print("x and y are in same address")
else :
    print("x and y are in different address..")
z=10
if(id(y)==id(z)):
    print("y and z are in same address")
else:
    print("y and z are in different address...")