'''
class product:
    def __init__(self,price):
        self.setprice(price)
    def setprice(self,price):
        if price<=0:
            raise ValueError("price cannot be negetive or zero...")
        self.price=price
p=product(12)
q=product(-123) 
'''
x=float(input())
a=int(x)
print(abs(x))