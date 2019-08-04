class parent:
    def __init__(self,name,idnum):
        self.name=name
        self.idnum=idnum 
        print("welcome")
    def pro(self):
        print("name : "+self.name)
        print("id number : "+self.idnum)
           
class child(parent):
    pass

n1=child("raka","180107")
n1.pro()