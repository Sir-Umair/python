# Problem # 1
class twoD:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"{self.i}i + {self.j}j")


class threeD(twoD):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k

    def show6(self):
        print(f"{self.i}i + {self.j}j + {self.k}k")


a = threeD(4, 5, 6)
a.show()
a.show6()

# Problem # 2
class animals:
    pass
class pets(animals):
    pass
class dog(pets):
    @staticmethod
    def dog():
        print("Bow Bow________!!!!!")
a=dog()
a.dog()

# Problem # 3
class employee:
    salary=345
    increment=30
    @property
    def salaryafter(self):
        return self.salary + (self.salary)*self.increment/100
    @salaryafter.setter
    def salaryafterq(self,salary):
        self.increment =  ((salary/self.salary) -1)*100 
e=employee()

print(e.salaryafter)
print(e.increment)

# Problem # 4
class complex:
    def __init__(self, r, i):
        self.i = i
        self.r = r

    def __add__(self, c2):
        return complex(self.r + c2.r, self.i + c2.i)

    def __mul__(self, c2):
        real_part = self.r * c2.r - self.i * c2.i
        imag_part = self.r * c2.i + self.i * c2.r
        return complex(real_part, imag_part)

    def __str__(self):
        return f"{self.r} + {self.i}i"

e = complex(4, 5)
r = complex(4, 9)
print("Addition:", e + r)
print("Multiplication:", e * r)

# Problem # 5
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        # Ensure `other` is a Vector before adding
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __mul__(self, other):
        # Dot product result is a scalar, not a Vector
        return self.x * other.x + self.y * other.y + self.z * other.z

    def __str__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"


# Creating vector objects
p = Vector(9, 7, 6)
d = Vector(1, 2, 3)
g = Vector(5, 4, 7)  # Provided correct 3 values

# Performing addition of two vectors at a time
sum_result = p + g + d  # This works because of chaining
dot_product = p * g  # Dot product of p and g

print("Sum of Vectors:", sum_result)      # Vector(15, 13, 16)
print("Dot Product of p and g:", dot_product)  # 122

# problem # 6
class Vector:
    def __init__(self, l): 
        self.l = l

    
    
    def __len__(self):
        return len(self.l)

# Test the implementation
v1 = Vector([1, 2, 3]) 
print(len(v1))
   