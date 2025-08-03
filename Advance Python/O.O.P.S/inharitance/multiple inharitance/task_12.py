class Myclass():
    def fun1(self):
        for i in range(1,6):
            print("*"*i)

class Myclass1():
    def table(self):
        n = int(input("enter number : "))

        for i in range(1,11):
            print(f"{n}*{i} = {n*i}")


class Myclass2(Myclass,Myclass1):
    def prime(self):
        n = int(input("enter number :"))
        
        prime1 = 0

        for i in range(1,n+1):
            if n%i==0:
                prime1+=1

        if prime1==2:
            print("number is prime!!")

        else:
            print("number is not prime!!")

obj = Myclass2()
obj.fun1()
obj.prime()
obj.table()