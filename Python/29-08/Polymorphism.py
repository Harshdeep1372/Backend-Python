class A:
    def show(self):
        
        print("Show From class A")
class B(A):
    def show(self):
        super().show()
        print("Show From class B")
class C(A):
    def show(self):
        super().show()
        print("Show From class C")
class D(B,C):
    def show(self):
        super().show()
        print("Show From class D")
c1=D()
c1.show()
    
