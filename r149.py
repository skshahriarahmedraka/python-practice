class A:
    def __init__(self,text):
        print("a ",text)
class B:
    def __init__(self,text):
        print("b ",text)
class C(B,A):
    def __init__(self,text):
        super().__init__(text)
        print("c ",text)
ca=C("ssar")
