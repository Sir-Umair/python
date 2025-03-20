# class test:
#     company = "Microsoft"
    
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

# # Object create karte waqt arguments pass karein
# object = test("UMAIR", 780000)

# # # Values print karne ke liye
# print(object.name)    # Output: UMAIR
# print(object.salary)  # Output: 780000
# print(object.company) # Output: Microsoft
# G = test("ZAIN",8790)
# print(G.name,G.company,G.salary)


# class calculator:
#     def __init__(self,n):
#         self.n=n
#     def square(self):
#         print(f"Suqare is:{self.n*self.n}")    
#     def cube(self):
#         print(f"Cube is: {self.n*self.n*self.n}")
#     @staticmethod
#     def greet():
#         print("Hello world")        
# r=calculator(7)
# r.square()
# r.cube()
# r.greet()

# class r:
#     a=6
# k=r()
# k.a=7
# #a will not change but instance of the class can be changed 
# print(k.a)

# from random import randint 

# class train:
#     def bookticket(self, to, fro, noofseat):
#         self.to = to
#         self.fro = fro
#         self.noofseat = noofseat
#         print(f"{self.fro} to {self.to} and {self.noofseat} seat(s) booked.")

#     def status(self):
#         print(f"You are going from {self.fro} to {self.to}. Number of seats: {self.noofseat}")

#     def fare(self):
#         print(f"Your fare is: {randint(455, 7888)} PKR")

# r = train()

# # Pehle ticket book karen
# r.bookticket("lahore", "faisalabad", 2)

# # Phir status aur fare check karen
# r.status()
# r.fare()


#IN PROBLEM NOTHING WAS AS SUCHH TO DO