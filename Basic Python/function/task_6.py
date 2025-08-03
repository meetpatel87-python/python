# 2) function with parameters without return type
#    parameters  -> user-input -> code -> function create
#    arguments  -> function call


def prime(n):   #parameters
    prime=0
    for i in range(1,n+1):
        if n%i==0:
            prime+=1

    if prime==2:
        print("prime!!")

    else:
        print("not prime!!")

n = int(input("enter number : "))

def add(a,b):
    print("addition : ",a+b)




prime(n)   #arguments

add(10,12)

