class A:
    def show(self):
        print("A's show method")

class B(A):
    def show(self):
        print("B's show method")

class C(A):
    def show(self):
        print("C's show method")

class D(B, C):
    pass

# Creating object of class D
d = D()
d.show()

# Let's print the MRO to inspect the order
print("Method Resolution Order:", D.__mro__)

# The MRO (Method Resolution Order) is the order in which Python looks for a method in a hierarchy of classes.
# In this case, the MRO for class D is:
# D -> B -> C -> A
# This means that when we call the show method on an instance of D, Python will first look in class D, then in class B, then in class C, and finally in class A.