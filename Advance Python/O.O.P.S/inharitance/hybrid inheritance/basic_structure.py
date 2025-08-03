class A():
    def fun1(self):
        print("method 1!!")

class B(A):
    def fun2(self):
        print("method 2!!")

class C():
    def fun3(self):
        print("method 3!!")

class D(B,C):
    def fun4(self):
        print("method 4!!")

obj = D()
obj.fun1()
obj.fun2()
obj.fun3()
obj.fun4()