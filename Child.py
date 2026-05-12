from Inheritance_Parent import Calculator


class Child(Calculator):
    num2=200

#It is necessary to call constructor from parent class to
#child class
    def __init__(self):
        Calculator.__init__(self,2,10)
    def getCompleteData(self):
        return (self.num2 + self.a + self.sum())

obj3=Child()

print(obj3.getCompleteData())
#200+2+(2+10+100)
