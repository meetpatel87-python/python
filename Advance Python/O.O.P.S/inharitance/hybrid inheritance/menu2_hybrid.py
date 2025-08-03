from menu_hybrid import *

obj = D()
obj.pattern()
obj.table()
obj.prime()

while True:
    menu ="""
    press 1 for pattern
    press 2 for prime number 
    press 3 for table
    press 4 for reverse
    press 5 for exit
    """

    print(menu)

    choice = int(input("enter choice : "))
 
    if choice==1:
        obj.prime()

    elif choice==2:
        obj.pattern()

    elif choice==3:
        obj.table()

    elif choice==4:
        s = input("enter name :")
        print(obj.rev(s))

    elif choice==5:
        print("thank you")
        break

    else:
        print("invalid!!")