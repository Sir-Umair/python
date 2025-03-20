class employee:
    def __init__(self):  # Fixed constructor name
        print("constructor")
        self.name = "UMAIR"  # Use self to define instance variables
        self.language = "English"

    def getinfo(self):  # Method should use self
        print(f"name is: {self.name} and other one is: {self.language}")

    @staticmethod
    def greet():
        print("good afternoon")    

# Creating an object of the class
obj = employee()
obj.language = "PURSHIAN"
print(obj.name, obj.language)


# Creating another object
obj1 = employee()
obj1.name = "janu"
obj1.language = "urdu"

# Calling methods
obj1.getinfo()  # No argument needed since self is used
obj1.greet()
print(obj1.name, obj1.language)
