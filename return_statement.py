def cube(num):
    num*num*num
cube(3)
#above function is not show anything

def cube2(num):
    num*num*num
print(cube2(3))
# the above function give you "None"

def cube3(num):
    return num*num*num

print(cube3(3))
# Now the function will give the result
result = cube3(4)
print(result)
# Now the function will give the result


def cube4(num):
    return num*num*num
    print("cool")
print(cube4(5))
# this case the "cool" string will never print becouse the function will break there

