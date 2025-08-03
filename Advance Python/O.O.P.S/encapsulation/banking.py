import random

ac_no = random.randint(1000000001,9999999999)
password = random.randint(1001,9999)

class Bank():
    def ac_register(self):
        name = input("enter your name : ")
        email = input("enter email : ")
        mobile = int(input("enter mobile : "))
        balance = 5000

        self.balance=balance
        self.name=name
        print("your account number is :" ,ac_no)
        print("your password is :",password)


    def deposit(self):
        damount = int(input("enter deposit amount : "))
        print("your deposit amount is :",damount)

        self.balance+=damount

    def withdraw(self):
        wamount = int(input("enter withdraw amount : "))
        print("your withdraw amount is :",wamount)

        if wamount > self.balance:
            print("invalid amount!!")

        else:
            self.balance-=wamount

    
    def check_balance(self):
        print(f"{self.name} your account balance is {self.balance}")



obj = Bank()

print("press 1 for create account")
print("press 2 for exit")

choice = int(input("enter choice :"))
if choice==1 :
    obj.ac_register()

    while True:

        menu ="""
                 press 1 for deposit amount
                 press 2 for withdraw amount
                 press 3 for check balance 
                 press 4 for exit
                 """  
        print(menu)
        choice1 = int(input("enter choice : "))
        if choice1==1 :
            obj.deposit()

        elif choice1==2:
            obj.withdraw()

        elif choice1==3:
            obj.check_balance()
        
        elif choice1==4:
            print("thank you!!")
            break

        else:
            print("invalid choice!!")

else:
    print("thank you!!")