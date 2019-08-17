class A:
    
    def __init__(self):
        raka=0
        pass
    def raka(self):
        print("raka")
        pass
r1=A()
print(hasattr(r1,"raka"))
print(getattr(r1,"raka"))