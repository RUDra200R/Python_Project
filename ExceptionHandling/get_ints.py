import sys


def getint(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except EOFError:
            sys.exit(1)
        except:
            print("invalid number entered, please try again")
        finally:
            print("the finally clause always executes")


first_number = getint("please enter first number:")
second_number = getint("please enter second number:")

try:
    print("{} divided by {} is {}".format(first_number, second_number, first_number / second_number))
except ZeroDivisionError:
    print("you can't divided by zero")
    sys.exit(2)
else:
    print("Division is successfully done")
