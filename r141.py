class point:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    @classmethod
    def Zero(cls):
        return cls(0,0,0)
    def draw(self):
        print(f"point : ({self.x},{self.y})")
    
point=point(4,5,6)
point.draw()
point=point.Zero()
point.draw()