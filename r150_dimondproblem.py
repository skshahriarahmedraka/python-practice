class grand:
    def __init__(self,text):
        print("grand : ",text)

    def prob(self,t2):
        
        print("grand : ",t2)

class mother(grand):
    def __init__(self,text):
        #super().__init__(text)
        print("mother : ",text)
    def prob(self,t2):
        super().prob(t2)
        print("grand : ",t2)
class father(grand):
    def __init__(self,text):
        #super().__init__("raka")
        print("father : ",text)
    def prob(self,t2):
        super().prob(t2)
        print("grand : ",t2)
class child(mother,father):
    def __init__(self,text):
        #super().__init__(text)
        print("child : ",text)
    def prob(self,t2):
        super().prob(t2)
        print("grand : ",t2)
q=child("ssar")
print("dimond : ")
q.prob("what")
#help(q)