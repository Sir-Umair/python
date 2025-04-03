# PROBLEM # 1
try:
    with open("1.txt" ,"r") as f :
        print(f.read())
except Exception as e:
    print(e)
try:
    with open ("2.txt","r") as f:
        print(f.read())
except Exception as e:
    print(e)

print("PROCEDURE IS DONE")                    

# PROBLEM # 2
l=[1,2,34,5,77,88,69,9]
for i,item in enumerate(l):
    if i==2 or i==3 or i==1:
        print(item)

# problem # 3
table=[]
n=int(input("ENTER A NUMBER: "))
table=[n*i for i in range(1,11)]
print(table)

# problem # 4
try:
    n=int(input("ENTER A NUMBER: "))
    b=int(input("ENTER A NUMBER: "))
    if b==0:
        print(f"infinity")
    raise ZeroDivisionError("you are also dividing by zero")     
except  Exception as v:
    print(v)       

# problem # 4    BY CODE WITH HARRY
try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print(a/b)
except ZeroDivisionError as v:
    print("Infinite")

# PROBLEM # 5
n = int(input("Enter tables number: "))
table = [n * i for i in range(1, 11)]  

with open("table.txt", "a") as file:
    file.write(f"\nTable of {n} is: {table}\n")  