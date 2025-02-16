def cel(f):
    C = 5 * (f - 32) / 9  # Uses f without overwriting it
    return C

f = float(input("ENTER TEMPERATURE IN FAHRENHEIT: "))  # Takes input outside the function
print(f"Temperature in Celsius: {round(cel(f), 2)}")  # Calls function correctly

print("a")
print("b",end="")
print("c")

print("HELLO WORLD")
def sum(n):
    if(n==1):
        return 1
    return sum(n-1) + n

print(sum(54))
