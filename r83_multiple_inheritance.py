class base1:
    def __init__(self):
        self.b1="base1"
        print(self.b1)
class base2:
    def __init__(self):
        self.b2="base2"
        print(self.b2)
class derived(base1,base2):
    def __init__(self):
        #base1.__init__(self)
        base2.__init__(self)
        print("derived")
d=derived()
b1=base1()
print("end")