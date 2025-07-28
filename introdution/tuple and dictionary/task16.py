import random

item_list= ["rock", "paper", "scissor"]
user_choice = input("enter your move = rock, paper, scissor = ")

comp_choice = random.choice(item_list)
print(f"user choice = {user_choice}, computer choice = {comp_choice}")



if user_choice == comp_choice:
    print("Both chooses same: = Match Tie")

elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper covers Rock = Computer Win")
    else:
        print("Rock smashes Scissor = You win")

elif user_choice == "Paper":
    if comp_choice == "Scissor":
        print("Scissor cuts paper, Computer Win")
    else:
        print("Paper covers rock, You win")

elif user_choice == "Scissor":
    if comp_choice == "Paper":
        print("Scissor cuts paper, You win")
    else:
        print("Rock smashes scissor, Computer win")

else:
    print("invalid choice")

