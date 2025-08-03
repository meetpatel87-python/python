class Myclass():
    def fun1(self):
        print("method 1!!")

class Myclass1():
    def fun2(self):
        print("method 2!!")

class Myclass2(Myclass,Myclass1):
    def fun3(self):
        print("method 3!!")

obj = Myclass2()
obj.fun1()
obj.fun2()
obj.fun3()