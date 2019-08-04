class student:
    def __iter__(self):
        print("iterator begin...")
        self.r=12
        return self
    def __next__(self):
        #x=self.r
        self.r+=1
        print("number is : "+str(self.r))
        return self.r
p1=student()
it=iter(p1)

print(next(it))

print(next(it))

print(next(it))

print(next(it))
print(next(it))
print(next(it))
