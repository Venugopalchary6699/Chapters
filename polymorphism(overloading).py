"""
POLYMORPHISM
      Implementing same thing in different ways.

      1). Overloading
      2). Overring

1). OVERLOADING:
       --> Operator overloading
       --> Method overloading

    Operator overloading:
          example:
              "+" used as concatination and addition
              If "+" is used in between strings than concatination will done.
              If "+" is is used between the integer than addition will be done.

    Method overloading:
          * Method name should be same.
          * Arguments must be different.

          Example:
              add()
              add(1,2)
              add(1,2,3)
"""

"""
       Operator overloading
"""
a = "name"
b = "is"
print(a+b)
aa = 2
bb = 4
print(aa+bb)
class MOeverloading():
    def display(self,a=None,b=None):
        print(a,b)
obj = MOeverloading()
obj.display()       # if we don't mention anything in that, it will take the default value(i.e. None and None)
obj.display(2)
obj.display(2,3)
