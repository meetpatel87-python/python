class A():
    def fun1(self):
        print("method 1!!")

class B(A):
    def fun2(self):
        print("method 2!!")

class C(B):
    def fun3(self):
        print("method 3!!")

obj = C()
obj.fun1()
obj.fun2()
obj.fun3()