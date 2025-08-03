n1 = int(input("enter number :"))


try:
    n1 = int(input("enter number 1:"))
    n2 = int(input("enter number 2:"))

    print("division :",n1/n2)

except ValueError as e:
    print(e)

except ZeroDivisionError as e:
    print(e)

    

