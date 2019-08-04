import array 
a=array.array("i",[1,2,53,64,7])
print(a)
newa=array.array(a.typecode,(i**2 for i in a))
print(newa)
x,y=newa.buffer_info()
print(x)
print(y)