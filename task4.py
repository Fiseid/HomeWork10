def some_function():
    try:
        a = int(input("Please type a number: "))
        b = int(input("Please type another number: "))
    except ValueError:
        print("It should be number")


    try:
        c = a ** 2 / b
    except ZeroDivisionError:
        print("You can't divide by zero")

    print(c)
some_function()


