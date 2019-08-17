class child:
    def age(self,age):
        self.age=age
        print("child age : "+str(self.age))
class parent(child):
    def age(self,age):
        self.age=age
        print("parent age : "+str(self.age))
a=child()
b=parent()
print("child is a subclass of parent : ",end="")
print(issubclass(child,parent))
print("parent is a subclass of child : ",end="")
print(issubclass(parent,child))

print("a is a instance of child :",end="")
print(isinstance(a,child))
print("b is a instance of parent : ",end="")
print(isinstance(b,parent))
