# A = {
#     "UMAIR": "GREAT",
#     "ABRAR": "SUPER"
# }

# k=input("ENTER THE WORD TO KNOW MEANING : ")
# print(A[k])
# S=set()
# K=input("ENTER SOME:")
# S.add(int(K))
# K=input("ENTER SOME:")
# S.add(int(K))
# K=input("ENTER SOME:")
# S.add(int(K))
# K=input("ENTER SOME:")
# S.add(int(K))
# K=input("ENTER SOME:")
# S.add(int(K))
# K=input("ENTER SOME:")
# S.add(int(K))
# K=input("ENTER SOME:")
# S.add(int(K))
# print(S)

# S=set()
# S.add(20)

# S.add(20.0)
# S.add(23)

# print(len(S))
# S=set()
# print(type(S))
# S={}
# print(type(S))

# S = {
#     "UMAIR": 45
# }

# NAME = 'UMAIR4'

# # Correct way to update the dictionary
# S.update({"UMAIR5": 65})

# # Get the value for NAME (which is 'UMAIR4', not found)
# print(S.get(f"{NAME}", 100))  # Output: 100

# # Print the dictionary and the value of NAME

# print(S.keys(),S["UMAIR"])
# print(S)  # Output: {'UMAIR': 45, 'UMAIR5': 65}
S={}
NAME=input("ENTER NAME IS :")
LANG=input("ENTER LANGUAGE:")
S.update({NAME:LANG})
NAME=input("ENTER NAME IS :")
LANG=input("ENTER LANGUAGE:")
S.update({NAME:LANG})
NAME=input("ENTER NAME IS :")
LANG=input("ENTER LANGUAGE:")
S.update({NAME:LANG})
NAME=input("ENTER NAME IS :")
LANG=input("ENTER LANGUAGE:")
S.update({NAME:LANG})
print(S)


