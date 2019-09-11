class node:
    def __init__(self,data):
        #self.priviousnode= None
        self.nodedata=data
        self.nextnode=None
class linkedlist:
    def __init__(self):
        self.root=None
    def insert(self,data,extranode=None):
        if extranode is None:
            extranode=self.root
        if self.root is None:
            self.root=node(data)
        else :
            if extranode.nextnode is None:
                extranode.nextnode=node(data)
            else:
                self.insert(data,extranode=extranode.nextnode)
            