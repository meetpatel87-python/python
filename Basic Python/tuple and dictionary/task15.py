import random

oridinal = random.randint(1,51)

while True:
    print("*********enter number between 1 to 50 range!!*******")

    choice = int(input("enter choice :"))

    if choice>50:
        print("invalid choice!!")
        break

    elif choice==oridinal:
        print("win!!")
        break

    elif oridinal>choice:
        print("original number is greatest!!")
        
    else:
        print("original number is smallest!!")
    