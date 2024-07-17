def translater():
    translation = ""
    string = input("Write your statement: ")
    for x in string:
        if x in "AEIOUaeiou":
            translation = translation + "t"
        else:
            translation = translation + x
    return translation
     

print(translater())
