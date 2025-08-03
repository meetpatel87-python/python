class Myclass():
    def fun1(self):
        print("method 1!!")

class Myclass2(Myclass):
    def fun2(self):
        print("method 2!!")

class Myclass3(Myclass):
    def fun3(self):
        print("method 3!!")


obj = Myclass2()
obj1 = Myclass3()
obj.fun1()
obj.fun2()
obj1.fun3()
    