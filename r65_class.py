'''class computer:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
    def con(self):
        print("raka pc :",self.cpu,self.ram)

c1=computer("ryzen 7",16)
c2=computer("thredripper","32")

c1.con()
c2.con()
'''
class worker:
    factory="dhaka"
    def __init__(self,name):
        self.name=name
    def work(self,wor):
        self.wor=wor
    def show(self):
        print("name : "+self.name+" , work : "+self.wor+" , factory : "+self.factory)
w1=worker("raka")
w2=worker("rakib")
w1.work("eng")
w2.work("doc")
w1.factory="mymensing"
w1.show()
w2.show()
worker.factory="chi"
w1.show()
w2.show()