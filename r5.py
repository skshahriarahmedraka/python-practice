class mamal :
    def walk(self,s):
        print(f"{s} walks")
class dog(mamal):
    pass

class cat(mamal):
    pass

dog1=dog()
dog1.walk("mamal")