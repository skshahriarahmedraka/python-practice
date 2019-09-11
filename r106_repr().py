import datetime
'''
t=datetime.datetime.now()
print(str(t))
print(repr(t))
'''
class date:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __repr__(self):
        return f"repr a: {self.a} b:{self.b}"
    def __str__(self):
        return f"str a: {self.a} b:{self.b}"
q=date(10,20)

print(str(q))
print(repr(q))