# 3) function without parameter with return type



def fun3():

    n =int(input("enter number : "))
    fac=1

    for i in range(1,n+1):
        fac*=i

    return fac



#result = fun3()
#print(result)

#    or

print(fun3())