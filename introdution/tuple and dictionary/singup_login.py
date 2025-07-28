import random

otp = random.randint(1001,9999)

d = {}

while True:
    menu = """

        press 1 for signup
        press 2 for login
        press 3 for forgot-password
        press 4 for exit
        
        """
    
    print(menu)

    choice = int(input("enter choice : "))

    if choice==1 :
        print("**********welcome to signup!!**********")
        name = input("enter name : ")
        email = input("enter email : ")
        mobile = int(input("enter mobile : "))
        password = int(input("enter password : "))
        cpassword = int(input("enter confirm password : "))

        if password==cpassword:
            d['email']=email
            d['mobile']=mobile
            d['password']=password

            print("singup successfully")

        else :
            print("password & confirm password does not match!!")

    elif choice==2:
        print("**********welcome to login!!**********")
        email = input("enter email : ")
        password = int(input("enter password : "))

        if d['email']==email:
            if d['password']==password:
                print("login sucessfully!!")

            else:
                print("password does not match!!")

        else:
            print("email does not match!!")

    elif choice==3:
        print("**********welcome to forgot-password!!**********")
        mobile = int(input("enter mobile : "))
        if d["mobile"]==mobile:
            print("your otp is :",otp)

            uotp = int(input("enter otp : "))
            if otp==uotp:
                password = int(input("enter new password : "))

                d['password']=password
                print("password updated successfully!!")
            else:
                print("invalid otp!!")

        else:
            print("mobile number does not exist!!")

    elif choice==4:
        print("thank you!!")
        break
    else:
        print("invalid choice!!")
        break