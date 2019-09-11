#ok linklist
class node:
    def __init__(self,data):
        self.previousnode=None
        self.nodedata=data
        self.nextnode=None
class linklist:
    def __init__(self):
        self.root=None
    def insert(self,data,extranode=None):
        if extranode is None:
            extranode=self.root
        if self.root is None:
            self.root=node(data)
            return
        else:
            if extranode.nextnode is None:
                extranode.nextnode=node(data)
                extranode.nextnode.previousnode=extranode
                return
            else:
                return self.insert(data,extranode=extranode.nextnode)
    def delete(self,data):
        extranode=self.root
        if extranode is None:
            print("linked list is empty")
        else:
            while(extranode):
                if extranode.nodedata==data:
                    extranode.nextnode.previousnode=extranode.previousnode
                    extranode.previousnode.nextnode=extranode.nextnode
                    return
                extranode=extranode.nextnode
    def showlist(self):
        extranode=self.root
        if extranode is None:
            print("linked list is empty")
        else:
            print("data of the node : ")
            while(extranode):
                print(extranode.nodedata)
                extranode=extranode.nextnode
    def showreverse(self):
        extranode=self.root
        if extranode is None:
            print("linked list is empty")
        else:
            print("data of the node(reverse) : ")
            li=[]

            while(extranode):
                li.append(extranode.nodedata)
                extranode=extranode.nextnode
            li.reverse()
            for i in range(len(li)):
                print(li[i])
    def searchlist(self,data):
        extranode=self.root
        if extranode is None:
            print("linked list is empty")
        else:
            print("searching the node : ")
            while(extranode):
                if data==(extranode.nodedata):
                    print("data is found")
                    return extranode.nodedata
                extranode=extranode.nextnode
            print("data is not found")

if __name__=="__main__":
    n=int(input("how many input you want to put:"))
    a=linklist()
    for i in range(n):
        a.insert(input())
    print("all data :")
    a.showlist()
    b=input("give a data to delete : ")
    a.delete(b)
    a.showlist()
    a.showreverse()
    a.searchlist("4")
