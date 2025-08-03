class A():
    def fun1(self):
        n = int(input("enter number : "))

        for i in range(1,11):
            print(f"{n}*{i} = {n*i}")

class B():
    def fun1(self):
        super().fun1()
        for i in range(1,6):
            print("*"*i)

class C(B,A):
    def fun1(self):
        super().fun1()
        n = int(input("enter number :"))
        
        prime1 = 0

        for i in range(1,n+1):
            if n%i==0:
                prime1+=1

        if prime1==2:
            print("number is prime!!")

        else:
            print("number is not prime!!")


obj = C()
obj.fun1()
