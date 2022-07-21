class chef:
    def cheff1(self):
        print("he make one")
    def cheff2(self):
        print("He make two")
    def chef3(self):
        print("He make three")

class chef1(chef):
    def extra(self):
        print("indian")


obj = chef1()
print(obj.cheff1())