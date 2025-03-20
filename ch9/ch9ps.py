# f=open("j.txt")
# content=f.read()
# if "twinkle" in content :
#     print("yes is")
#     f.close()


# import random
# def game(): 
#     print("You are playing the game..")
#     score = random.randint(1, 62)
#     # Fetch the hiscore
#     with open("hiscore.txt") as f:
#         hiscore = f.read()
#         if(hiscore!=""):
#             hiscore = int(hiscore)
#         else:
#             hiscore = 0

#     print(f"Your score: {score}")
#     if(score>hiscore):
#         # write this hiscore to the file
#         with open("hiscore.txt", "w") as f:
#             f.write(str(score))

#     return score

# game()

def generatetable(n):
    n = int(input("ENTER THE TABLE NUMBER: "))
    print(f"You entered: {n}")

    with open("table.txt", "w") as f:  # Corrected file opening
        for i in range(1, 11):
            k = f"{n} X {i} = {n * i}\n"  # Generate table row
            print(k)  # Print each row
            f.write(k)  # Write to file

# Call the function with a user-provided number
generatetable(6)



