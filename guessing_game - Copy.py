secrete_word = "lion king"
guess = ""
i = 1
while secrete_word != guess and i <=3:
    guess  = input("enter the guess : ")

    if guess == secrete_word:
        print("you got the word: " + guess)
    elif i < 3:
        print("incorect guess again")
    else:
        print("katham tata bye bye good bye")
    i +=1

