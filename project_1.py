import random

def play_game():
    print("Welcome to Snake-Water-Gun Game!")
    print("Rules: s for Snake, w for Water, g for Gun\n")

    youDict = {"s": 1, "w": -1, "g": 0}
    reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}
    
    user_score = 0
    comp_score = 0
    rounds = 0

    while True:
        youstr = input("Enter your choice (s/w/g) or 'q' to quit: ").lower()

        if youstr == 'q':
            print("\nGame Over!")
            print(f"Final Score => You: {user_score}, Computer: {comp_score}")
            if user_score > comp_score:
                print("🎉 You won the match!")
            elif comp_score > user_score:
                print("😞 You lost the match!")
            else:
                print("🤝 It's a draw overall!")
            break

        if youstr not in youDict:
            print("Invalid choice! Please enter 's', 'w', or 'g'.")
            continue

        you = youDict[youstr]
        computer = random.choice([-1, 0, 1])

        print(f"\nYou chose: {reverseDict[you]}")
        print(f"Computer chose: {reverseDict[computer]}")

        if computer == you:
            print("Result: It's a draw!\n")
        elif (computer == -1 and you == 1) or (computer == 0 and you == -1) or (computer == 1 and you == 0):
            print("Result: You win this round!\n")
            user_score += 1
        else:
            print("Result: You lose this round!\n")
            comp_score += 1

        rounds += 1
        print(f"Score => You: {user_score}, Computer: {comp_score}")
        print(f"Rounds Played: {rounds}\n")

# Run the game
play_game()
