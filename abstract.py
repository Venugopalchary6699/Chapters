# THE METHOD ONLY HAVE DICLARATION NOT HAVE ANY DEFINATION IS CALLED ABSTRACT METHOD

"""
To impliment abstract class there is module we have to import
that is "abc module"

we have to import abc class and abstract method

we use abstract method as a decorator
"""
"""
method with a declaration not defination
"""

"""
class without abstract method colled concretre class
"""

"""
object cant be instantiated for abstract class
object can be instantiated for concrete class
"""

"""
import abc module

class aclass(ABC):
  @abstractmethod
  def display(self):
  None
  
class demo(aclass):
   def display(self):
      print("abstract method)
"""

from abc import ABC, abstractmethod

class abstractdemo(ABC):     #ABSTRACT CLASS
    @abstractmethod          #ABSTRACT METHOD
    def display(self):
        None
    @abstractmethod          #ABSTRACT METHOD
    def show(self):
        None

class demo(abstractdemo):
    def display(self):
        print("MTHIRD OF ABSTRACT CLASS")
    def show(self):
        print("show absract method")
class demo1(abstractdemo):
    def show(self):
        print("show absract method")
    def display(self):
        print("MTHIRD OF ABSTRACT CLASS")



obj = demo()
obj.display()
obj.show()
obj1 = demo1()
obj1.show()
obj1.display

"""
MY WORDS
   
   The class which have declaration but dont have defination
   
   we have to inherate the abstract class in concrete class to define the abstract class
   
   if the concrete class fails to define any one of abstract class the concrete class become abstract class
"""