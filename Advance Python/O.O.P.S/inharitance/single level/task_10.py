class A:
    def fun1(self):
        n = int(input("enter number : "))
 
        sum=0
        for i in range(0,n+1):
    
             sum = sum + i
                #0+1 = 1+2 = 3+3 = 6+4 = 10+5 = 15
     
        print(sum)

    def fun2(self):
        n = int(input("enter number : "))

        if n<0:
            print("enter positive number!!")

        else:

            if n==1 or n==2 or n==3:
                print(n,"is prime!!")

            else:
                prime = 0
                for i in range(1,n+1):

                    if (n%i==0):
                        prime+=1

            if prime==2:
             print(n,"is prime number!!")

            else:
                print(n,"not a prime number!!")

class B(A):
    def fun3(self):
        n = int(input("enter number : "))
        fac = 1
        i = 1
        while(i<=n):
            fac=fac*i
            i=i+1

        print(fac)

obj = B()
obj.fun1()
obj.fun2()
obj.fun3()