
def display(a,b):
    print(a, b)

display(22, 33)

def display(name,course = "B-Tech"):

    print(name, course)

display("name2", "M-Tech")
display("name3")


def display3(*names):
    print(names)
    for i in names:
        print(i)

display3("name1", "name2", "nmae3", "name4", "name5", "name6")