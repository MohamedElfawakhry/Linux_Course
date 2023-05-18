
myTuple = ("1.Startswith()" , "2.Title()" , "3.isspace()")


print(myTuple)
choose = int(input("To Understand any of these function choose it's number :"))
while choose != 27:
    if(choose == 1):
        print(''' Check if the string starts with "Hello":
        this is the running code :
        txt = "Hello, welcome to my world."

        x = txt.startswith("Hello")

        print(x)
        ''')
        txt = "Hello, welcome to my world."

        x = txt.startswith("Hello")

        print(x)
    elif (choose == 2):
        print(''' Make the first letter in each word upper case:
        this is the running code :
        txt = "Welcome to my world"

        x = txt.title()

        print(x)
        ''')
        txt = "Welcome to my world"
        x = txt.title()

        print(x)

    elif(choose == 3 ):
        print(''' Check if all the characters in the text are whitespaces:
        this is the running code :
        txt = "   "

        x = txt.isspace()

        print(x)
        ''')
        txt = "   "
        x = txt.isspace()
        print(x)
    print(myTuple)
    choose = int(input("To Understand any of these function choose it's number :"))