class tagcloud:
    def __init__(self):
        self.dic={}
        self.__dic2={"raka":"1","ssar":"2"}
    def adddic(self,tag):
        self.dic[tag.lower()]=self.dic.get(tag.lower,0)+1
    def __getitem__(self,tag):
        return self.dic.get(tag.lower())
    def __setitem__(self,tag,count):
        self.dic[tag.lower()]=count
    def __iter__(self):
        return iter(self.dic)

cloud=tagcloud()
print(cloud._tagcloud__dic2)