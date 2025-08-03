class Myclass():
    def fun1(self):
        print("method 1!!")

class Myclass2(Myclass):
    def fun1(self):
        super().fun1()
        print("method 2!!")

obj = Myclass2()
obj.fun1()
