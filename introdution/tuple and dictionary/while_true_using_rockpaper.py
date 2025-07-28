import random

item_list = ["rock", "paper", "scissor"]

# User ni ichchha pramane rounds
rounds = int(input("Ketla round ramva che? Enter number of rounds: "))

for i in range(rounds):
    while True:
        user_choice = input("Enter your move (rock, paper, scissor): ").lower()
        if user_choice in item_list:
            break
        else:
            print("Invalid choice! Please enter rock, paper, or scissor.")

    comp_choice = random.choice(item_list)
    print(f"\nRound {i+1}: You chose {user_choice}, Computer chose {comp_choice}")

    if user_choice == comp_choice:
        print("Both chose same = Match Tie")

    elif user_choice == "rock":
        if comp_choice == "paper":
            print("Paper covers rock = Computer wins")
        else:
            print("Rock smashes scissor = You win")

    elif user_choice == "paper":
        if comp_choice == "scissor":
            print("Scissor cuts paper = Computer wins")
        else:
            print("Paper covers rock = You win")

    elif user_choice == "scissor":
        if comp_choice == "rock":
            print("Rock smashes scissor = Computer wins")
        else:
            print("Scissor cuts paper = You win")

    print("-" * 30)

