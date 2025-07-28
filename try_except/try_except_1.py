try:
    n = int(input("enter number :"))

    print(n)

    if n>0:
        print("positive!!")
except ValueError as e:
    print(e)



else:
    print("try excecuted!!")
    print("except excecuted!!")

finally:
    print("finally excecuted!!")
