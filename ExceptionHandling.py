try:
    x= int(input("first number: "))
    y= int(input("second number: "))
    x/y
except ZeroDivisionError as e :
    print("you can't divide by zero\n")

except ValueError:
    print("you must enter numbers only\n")

except:
    "something went wrong\n"

       