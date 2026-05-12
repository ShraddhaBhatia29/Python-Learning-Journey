class Calculator:
    num=100
    def __init__(self,a,b):
        print("I am called auto when any new object is created")
        self.a=a
        self.b=b
    def getdata(self):
        print("I am executing method in class")
    def sum(self):
        return (self.a + self.b+Calculator.num)

obj1=Calculator(2,3)
obj2=Calculator(4,5)
obj1.getdata()   #object calling method
print(f"Sum is {obj1.sum()}")
print(obj2.sum())
print(obj1.num)
