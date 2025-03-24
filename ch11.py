# class parent:
#     print("parent class")
# class child(parent):
#     print("child class")
# r=child()

# class Parent:
#     name = "Umair"

#     def show(self):
#         print(f"parent: {self.name}")

#     print("HERE IS THE PARENT CLASS.......")

# class Child(Parent):
#     def __init__(self):
#         print("HERE IS THE CHILD CLASS.........")

#     def get(self):
#         self.a = input("Enter something: ")
#         print(self.a)

# class Grandchild(Child):
#     def __init__(self):
#         super().__init__()  # Ensures the Child constructor is called
#         print("GRAND CHILD CLASS........")

#     def give(self):
#         self.K = input("Enter something else: ")
#         print(self.K)

# a = Grandchild()
# a.show()
# a.get()
# a.give()

# class A:
#     def show(self, a, b):  # Remove 'int' type annotations
#         self.a = a
#         self.b = b
#         print(self.a, self.b)
# class B(A):
#     def shew(self):
#         self.a="Ali"
#         self.b="Umair"
#         print(self.a,self.b)
# class C(A):
#     def shown(self):
#         self.a="bhai"
#         self.b="aja" 
#         print(self.a, self.b)      

# # Creating an instance of the class
# obj=C()
# obj.show(6,8)
# obj1=B()
# obj1.shew()
# obj.shown()

# class A:
#     a = 5
#     print(a)  # Executes when the class is defined

# class B(A):
#     def __init__(self):
#         print("hello from B")
        

#     b = 6
#     print(b)

# class C(B):
#     def __init__(self):
#         print("hello from C")
#         super().__init__()  # Calls the constructor of B

#     c = 8
#     print(c)

# # Creating an instance of the most derived class (C)
# obj = C()

# # Accessing all attributes
# obj.a  # Inherited from A
# obj.b  # Inherited from B
# obj.c  # From C


class abc:
    a = 6

    @classmethod
    def ag(cls):
        print(f"VALUE OF A IS: {cls.a}")

    @property
    def abc(self):
        return f"{self.fname} {self.lname}"  # Correct f-string syntax

    @abc.setter
    def abc(self, value):
        self.fname = value.split(" ")[0]  # First name
        self.lname = value.split(" ")[1]  # Last name

g = abc()

g.a = 76
g.ag()  # Class method, so called normally with parentheses

# Using the setter to change the value
g.abc = "Ali Khan"  # Setter is called here

print(g.abc)  # Output: Ali Khan

class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):
        return self.n + num.n

n = Number(1)
m = Number(2)

print(n + m)