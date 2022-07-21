"""
METHOD OF OVERRIDE:

       Father rides bi-cycle
       Son rides bike

       * Method name should be same
       * Number of arguments should be same
"""


class father:
    def transportation(self):
        print("bi-cycle")

class son:
    def transportation(self):
        print("bike")

obj = son()
obj.transportation()

