# # Using walrus operator 
# if (n := len([1, 2, 3, 4, 5])) > 3: 
#     print(f"List is too long ({n} elements, expected <= 3)") 

# # Type Definition
# a: int = 4
# k: str = "Umair"
# print(f"{a}:{k}=/////")

# from typing import List, Union, Tuple 

# p: Union[int, str] = "e6uyuyuyuu66767"

# def sum(g: int, l: int):
#     return g + l

# print(sum(9, 87))

# # Match-Case
# a = int(input("ENTER A VALUE: "))
# match a:
#     case 1:
#         print("one")
#     case x if 0 <= x <= 9:
#         print("two")
#     case _:
#         print("Jado")

# # Match-Case Function
# def http_status(status): 
#     match status:  
#         case 200: 
#             return "OK" 
#         case 404: 
#             return "Not Found" 
#         case 500: 
#             return "Internal Server Error" 
#         case _: 
#             return "Unknown status"  

# print(http_status(5007))

# # Merge dictionary properly
# a = {"k": 3, "j": 9}
# b = {"b": 5, "x": 43}
# merged = a | b
# print(merged)

# # Exception Handling
# try:
#     a = int(input("Hey, Enter a number: "))
#     print(a)

# except ValueError as v:
#     print("Heyyyy")
#     print(v)
    
# except Exception as e:
#     print(e) 

# print("Thank You")

# # raise exception
# a= int(input("Enter a Number: "))
# b= int(input("Enter seconed Number: "))
# if b==0:
#     raise ZeroDivisionError("THIS IS INFINITY")
# else:
#     print(f"{a/b}")

# # TRY WITH ELSE    
# try:
#     a=int(input("Enter a number: "))
#     print(a)
# except Exception as e:
#     print(f"heyy :{e}")
# else:
#     print("NA KR MERA BHAI")

# # try with final
# try:
#     a=int(input("Enter a number: "))
#     print(a)
# except Exception as e:
#     print(f"heyy :{e}")
# finally:
#     print("i am final and will run in every single case")

# # main with module
# def myfunc():
#     print("HELLO WORLD")

# if __name__ == "__main__":  # ✅ Corrected from "ch12" to "__main__"
#     myfunc()
#     print(__name__)    
#     print("You are running from the main.....")


# # global variables
# a =56

# def my_function():
#     a = 6  
#     print(a)  # Output: 6

# my_function()
# print(a)

# # enumerate
# l=[1,2,34,5]
# for index,item in enumerate(l):
#     print(f"{index} and: {item}")
