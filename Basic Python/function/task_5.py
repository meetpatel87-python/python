import math
# 1) function without parameters without return type
def signup():

    for i in range(1,6):
        print("*"*i)


def fac():
    n = int(input("enter number : "))

    print(math.factorial(n))


signup()

fac()