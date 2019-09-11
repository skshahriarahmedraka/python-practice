class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __eq__(self,other):
        return self.x==other.x and self.y==other.y
    def __add__(self,other):
        return point(self.x+other.x , self.y +other.y)

a=point(12,23)
b=point(12,23)
print(a==b)
a.x=32
print(a==b)
b=a+b
print(f"a : {b.x} and b : {b.y}")
