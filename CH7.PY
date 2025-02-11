Your handwritten program appears to be:

L = ["a", "b", "c", "d"]

def ajc():
    for i in range(len(L)):  # Looping using len(L)
        print(L[i])  # Printing each element by index

ajc()

Explanation:

L is a list containing ["a", "b", "c", "d"].

len(L) returns 4, so range(len(L)) generates [0, 1, 2, 3].

The for loop iterates over these indices, accessing L[i] and printing the elements.


Expected Output:

a
b
c
d

If you want to include the index in the output, modify the print statement:

print(f"Index {i}: {L[i]}")

Let me know if you need changes!

# i=0
# while(i<6):
#     print(i)
#     i=i+1

# l = [1, "Harry", False, "This", "Rohan", "Shubham", "Shubhi"]

# index = 0

# while(index<len(l)):
#     print(l[index])
#     index +=1
# l=[1,"index",5,69,25,36]
# for i in l:
#     print(i)
# else:print("done")
for i in range(1, 50, 5):  # Loop from 1 to 49, incrementing by 5
    if i == 45:
        continue  # Skip printing 45

    print(i)  # Print i
