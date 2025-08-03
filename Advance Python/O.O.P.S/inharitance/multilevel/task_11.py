class A:
    def fun1(self):
        self.name = input("enter your name : ")
        self.roll = int(input("enter your roll number(1-100) : ",))


class B(A):
    def fun2(self):
        self.math =int(input("enter your maths mark(1-100) : "))
        self.sci = int(input("enter your science mark(1-100) : "))
        self.guj = int(input("enter your gujrati mark(1-100) : "))
        self.eng = int(input("enter your english mark(1-100) : "))
        
class C(B):
    def fun3(self):
        total_mark = self.math + self.sci + self.guj + self.eng
        percentage = total_mark*100/400
        print(f"percentage : {percentage:.2f}% ")

        if percentage > 75:
            print("first class!!")

        
        else:
            print("You have not achieved First Class!!")
obj = C()
obj.fun1()
obj.fun2()
obj.fun3()
