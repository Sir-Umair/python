# F = open("fz.txt")  # File name should be in quotes
# data = F.read()
# print(data)
# F.close()  # Use the same variable name to close the file

#I`M` GOING TO CREATE A NEW FILE WITHOUT TRADITIONAL METHOD
# F=open("master.txt","w")
# st="UMAIR RAMZAN MUBARIK"
# F.write(st)
# F.close()

#more function
f=open("fz.txt")
# f.readline()
# line2=f.readline()
# print(line2,type(line2))
# f.close()

#loop to open file 
# line = f.readline()
# while(line != ""):
#     print(line)
#     line = f.readline()

# f.close()
with open("fz.txt"):
    print(f.readline())