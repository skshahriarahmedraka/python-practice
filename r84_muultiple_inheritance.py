class area:
    def __init__(self,l,m):
        self.l=l
        self.m=m
    def a(self):
        print(self.l*self.m)

class rectangle(area):
    def __init__(self,l,m):
        super().__init__(l,m)

    def ar(self):
        super().a()
    
q=rectangle(12,12)
q.ar()