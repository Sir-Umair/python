name = input("Enter name: ")
marks = int(input("Enter marks: "))
phone = int(input("Phone number: "))

s = "The name of the student is {}, his marks are {} and phone number is {}".format(name, marks, phone)

print(s)

# problem # 2
n = int(input("ENTER TABLE NAME: "))
k = [str(n * i) for i in range(1, 11)]
s = "\n".join(k)
print(s)

# problem 3 
def div(n):
    if n%5==0:
        return True
    else:
        return False
a=[4,5,6,77,88,55,45,25]
k=list(filter(div,a))
print(k)
 
from functools import reduce
l=[4,5,6,77,88,55,45,25]
def gh(a,b):
    if a>b:
        return a
    return b
b=reduce(gh,l)
print(b)
# problem # 4

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

app.run()