def translater(phrase):
    translation = ""
    for index in phrase:
        if index in "aeiouAEIOU":
            if index.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"

        else:
            translation = translation + index
    return translation

print(translater(input("inter a word : ")))