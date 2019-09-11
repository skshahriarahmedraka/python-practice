'''
le=["a","b","c","d","c"]
if "b" in le:
    print(le.index("b"))
print(le.count("c"))
li=[1,3,2,5,463,7,3,8,55]
print(sorted(li))
print(sorted(li,reverse=True))
print(li)
'''
'''
def item(data):
    return data[1]
li=[("rakia",4),("shahin",3),("raki",9)]
li.sort(key=item)
print(li)
'''

li2=[("ad",3),("dd",34),("aa",87)]
li2.sort(key=lambda x:x[1])
print(li2)
