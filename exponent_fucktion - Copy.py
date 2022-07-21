def rais_tothepower(base_num, pow_num):
    result = 1

    for index in range(pow_num):
        result = result * base_num
    return result

print(rais_tothepower(2, 3))

def some_thing():
    for index in range(10):
        print("cool")
#this is new understanding
some_thing()