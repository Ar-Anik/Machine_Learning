# type1
num1 = input("Enter 1st number :: ")
num2 = input("Enter 2nd number :: ")

try :
    division = int(num1)/int(num2)
except Exception as a :
    print("Exception occur :: ", a)
    division = None

print("Division : ", division)

# type2
num1 = input("Enter 1st number : ")
num2 = input("Enter 2nd number : ")

try :
    division = int(num1)/int(num2)
except ZeroDivisionError as a :
    print("Division By Zero")
    division = None

print("Division : ", division)

# Exception type name
num1 = input("Enter 1st Number : ")
num2 = input("Enter 2nd Number : ")

try :
    division = num1/int(num2)
except Exception as a :
    print("Error Type : ", type(a).__name__)
    division = None

print("Division : ", division)