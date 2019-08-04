import array,numpy
i=array.array("d",[12.234,55.24,53.34,64.46,23.1])
print(i)
'''i1=array.array("Q",[[12,43,34],[1,3,5],[2,4,6]])#for numpy
print(i1)'''
print(array.typecodes)
print(i.typecode)
i3=array.array(i.typecode,(x**2 for x in i))
print(f"element are {i3}")


ii=array.array("i",[1,2,5,3,6,7,5,1,99,7])
ii2=array.array("i",[0,1,-1,-2,-3,-7])
print(ii.count(5))
ii.extend([11,22,33,44,55])
print(ii)
ii.extend(ii2)
print(ii)
li=[111,222,333]
ii.fromlist(li)
print(ii)
#uni=array.array("")
t=ii.buffer_info()
print(t)
ii.byteswap()
print(ii)
uniarr=array.array("u","raka")
print(uniarr)
to=ii.tobytes()
print(to)