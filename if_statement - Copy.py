"""
by using if statement i exicute sertain code when cerrein condition are tue
"""

is_male = 5

if is_male:
    print("King")
if is_male is True:
    print("king2")
elif is_male == 5:
    print("king kong")
else:
    print("you not a male")

iss_male = False
is_tall = False

if is_male or is_tall:
    print("M or L")
elif is_male and is_tall:
    print("M and L" )
else:
    print("Female")

