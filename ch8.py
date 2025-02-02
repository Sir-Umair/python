# def avg(N,V):
#     k = input("ENTER NAME ")  # Get user input
#     print(f"Have a good day, {k}: {N} {V}")  # Use f-string for formatting

#     return "done"
# A=avg("KASHI",4)
# print(A)
def k(NAME, ENDING="THANK YOU"):  
    print(f"HAVE A GOOD DAY: {NAME}")
    print(ENDING)

k("UMAIR", "THANKS")  # Function call should match lowercase 'k'


#RECURSIONS
# def factorial(n):
#     if(n==1 or n==0):
#         return 1
#     return n * factorial(n-1)


# n = int(input("Enter a number: "))
# print(f"The factorial of this number is: {factorial(n)}")





def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Example usage
n=int(input("ENTER THE NUMBER: "))
print(f"Factorial of {n} is {factorial(n)}")
# HINT THIS IS FUNCTIONCAL {factorial(n)}