# ===============================
# OOPS BASICS – CLASS & OBJECT
# ===============================

class Calculator:
    num = 100  # class variable

    def getdata(self):
        print("I am executing method in class")


# Creating object of Calculator class
obj = Calculator()
obj.getdata()
print(obj.num)

print("\nANOTHER EXAMPLE......")

# ===============================
# CLASS WITH CONSTRUCTOR
# ===============================

class Dog:
    species = "Canine"  # class variable

    def __init__(self, name, age):
        self.name = name      # instance variable
        self.age = age        # instance variable


# Creating object of Dog class
dog_montu = Dog("Montu", 1)

print(dog_montu.name)
print(dog_montu.age)


# ===============================
# CONSTRUCTOR EXAMPLE
# ===============================

class Calculator:
    num = 100

    def __init__(self, a, b):
        print("I am called automatically when object is created")
        self.a = a
        self.b = b

    def getdata(self):
        print("I am executing method in class")

    def sum(self):
        return self.a + self.b + Calculator.num


obj1 = Calculator(2, 3)
obj2 = Calculator(4, 5)

obj1.getdata()
print(f"Sum is {obj1.sum()}")
print(obj2.sum())

print("\nself keyword is necessary when creating methods inside a class")


# ===============================
# PRACTICE EXAMPLE
# ===============================

class Dogs:
    color = "black"  # class variable

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def tell_name(self):
        return self.name


dog1 = Dogs("Poofy", "Labrador")
dog2 = Dogs("Tuffy", "Labrador")

print(dog1.tell_name())
print(dog2.tell_name())

print("\nInstance variables are defined inside methods")
print("Class variables are defined in the class and shared")
print("Constructor name in Python is __init__")
``
