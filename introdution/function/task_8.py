# 4) function with parameter with return type



def prime(n):   #parameters
    prime=0
    for i in range(1,n+1):
        if n%i==0:
            prime+=1

    if prime==2:
        print("prime!!")

    else:
        print("not prime!!")
    return prime

n = int(input("enter number : "))

prime(n) #argument
print(n)