'''
li=[1,2,3,4,5]
li3=[2,3,4,5]

li2=list(map(lambda x: x+3 ,li ))
print(li2)

li2=list(map(lambda x,y:x+y ,li,li3))
print(li2)

li4=["sat","sun","mon","tues"]
li5=list(map(list,li4))
print(li5)
'''
class BstNode:

    def __init__(self, key):
        self.key = key
        print("inputed "+str(key))
        self.right = None
        self.left = None

    def insert(self, key):
        if self.key == key:
            return
        elif self.key < key:
            if self.right is None:
                self.right = BstNode(key)
            else:
                self.right.insert(key)
        else: # self.key > key
            if self.left is None:
                self.left = BstNode(key)
            else:
                self.left.insert(key)

a=BstNode(12)
a.insert(11)
a.insert(15)
a.insert(12)