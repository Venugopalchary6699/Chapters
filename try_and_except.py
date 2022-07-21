x = 1
while x:
    try:
        number = int(input("enter a number: "))
        print(number)
        x -= 1
    except:
        print("invalid input")


try:
    number = int(input("enter a number: "))
    print(number)
    x -= 1
except Zerodivisionerror as err:
    print(err)
except ValueError:
    print("invalid input")
    
