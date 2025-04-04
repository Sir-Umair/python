from functools import reduce
# def square(x):
#     return x*x
square=lambda x:x*x
print(square(3))
square=lambda x=3:x*x
print(square())

# join function
a=["UMAIR","ABRAR"]
final="::".join(a)
print(final)

# STRING FORMAT
a="{0} is a good boy {1}".format("Umair","g")
print(a)

# map function
j=[3,4,5,6]
square=lambda x:x*x
sql1=map(square,j)
print(list(sql1))

# filter function
def even(n):
    if n%2==0:
        return True
    return False
onlyeven=filter(even,j)
print(list(onlyeven))

# reduce function
def sum(a,b):
    return a+b
print(reduce(sum,j))