"""
ENCAPSULATION:
     Wrapping up of data is called encapsulation.

     wrapping up of data means combining the methods and variables in a single place

     We can achieve the encapsulation by restricting the scope of variables and methods to the class

     if you mention "__" as a prefix the variable or method become private
     private means the scope is restricted withing the class(private variable)

"""

class encap:
    a = 10
    def __display(self):
        print("welcome")
        print(self.a)

obj = encap()
obj.display()


