


class method():
    def m(self,a=None,b=None):
        print(a,b)

obj = method()
obj.m()
obj.m(4,4)



class father():
    def transportation(self):
        print("cycle")
class son(father):
    def transportations(self):
        print("bike")



obj = father()
obj2 = son()
obj2.transportation()
obj2.transportations()
obj.transportation()
obj.transportation()

from abc import ABC, abstractmethod
class abstractdemo(ABC):
    @abstractmethod
    def display(self):
        None
    @abstractmethod
    def show(self):
        None
class demo(abstractdemo):
    def display(self):
        print("good")
    def show(self):
        print("good day")

obj3 = demo()
obj3.display()
obj3.show()
