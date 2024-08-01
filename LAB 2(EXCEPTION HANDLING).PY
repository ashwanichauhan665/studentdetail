
#write a python program that opens a file and handles a FileNotFoundError exception if the file does not exist.
with open("abc.txt","w") as file:
    file.write("india ")

filename = 'abc.txt'

try:
    with open(filename, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError :
     print("file does not exists.")

#write a python program that prompts the user to input two numbers and raise a typeError exception is the inputs are not numerical
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

try:
    # Convert inputs to float
    num1 = float(num1)
    num2 = float(num2)

    print("The sum of numbers are : ",num1+num2)

except ValueError:
    raise TypeError("Both inputs must be numerical values.")

#write a python program that prompts the user to input an integer and raise a ValueError Exception if the input is not a valid integer.

user_input=input("Please enter an integer : ")
try:
    value = int(user_input)
    print("you entered the integer : ",value)
except ValueError :
    raise ValueError("Invalid input : Please enter a valid integer.")  

#write a python program to handle a ZeroDivisionError exception when dividing a number by Zero.

def divide(a,b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        print(e)
    
    return result
print(divide(46,2))
print(divide(10,0))    