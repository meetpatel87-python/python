from diff_class1 import *

obj = Prime()
obj1 = Pattern()
obj2 = Table()
obj3 = Reverse()
while True:
    menu ="""
    press 1 for prime number 
    press 2 for pattern
    press 3 for table
    press 4 for reverse
    press 5 for exit
    """

    print(menu)

    choice = int(input("enter choice : "))
 
    if choice==1:
        obj.prime()

    elif choice==2:
        obj1.pattern()

    elif choice==3:
        obj2.table()

    elif choice==4:
        s = input("enter name :")
        print(obj3.rev(s))

    elif choice==5:
        print("thank you")
        break

    else:
        print("invalid!!")