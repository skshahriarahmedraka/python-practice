class stack:
    def __init__(self):
        self._data=[]
    def len(self):
        return len(self._data)
    def is_empty(self):
        return len(self._data)==0
    def push(self,data):
        self._data.append(data)
    def top(self):
        if len(self._data)==0:
            print("stack is empty")
            return
        return self._data[-1]
    def pop(self):
        if len(self._data)==0:
            print("stack is empty")
        return self._data.pop()

 def main()
if __name__=="__main__":
    main()
    

