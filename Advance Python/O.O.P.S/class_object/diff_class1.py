class Prime:
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

class Pattern:
    def pattern(self):
        for i in range(1,6):
            print("*"*i)

class Table:
    def table(self):
        n = int(input("enter number : "))

        for i in range(1,11):
            print(f"{n}*{i} = {n*i}")


class Reverse:
    def rev(self,s):

        if len(s)%2==0:
            print(s)

        else:
            mid = len(s)//2
            return mid