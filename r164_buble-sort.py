class node:
    def __init__(self,data):
        self.previousNone=None
        self.nodedata=data
        self.nextnode=None
class linklist:
    def __init__(self):
        self.root=None
    def insert(self,data,extranode=None):
        
        
        if extranode is None:
            extranode=node(data)
            if self.root is None:
                self.root=extranode
            return extranode

        else:
            self.insert(data,extranode=extranode.nextnode)
    def showlist(self):
        extranode=self.root
        while(extranode):
            print(extranode.nodedata)
            extranode=extranode.nextnode

if __name__=="__main__" :
    n=int(input("how many data(insert) : "))
    a=linklist()
    for i in range(n):
        a.insert(input())
    print("all the data are : ")
    a.showlist()
