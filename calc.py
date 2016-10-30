import sys

def first_int():
    global org
    org = input("Enter a number:")
    if org.isalpha():
        sys.exit
    else:
        symbol()

def symbol():
    global sym
    sym = input("Enter:\n+ for addition\n- for substraction\n* for multiplication\n/ for divide:")
    if sym == "+" or sym == "-" or sym == "*" or sym == "/":
        second_int()
    else:
        symbol()

def second_int():
    global num2
    num2 = input("Enter second number:")
    if num2.isalpha():
        print("Invalid!")
        second_int()
    else:
        result()

def result():
    if sym == "+":
        print (float(org) + float(num2))
        first_int()
    if sym == "-":
        print(float(org) - float(num2))
        first_int()
    if sym == "*":
        print(float(org) * float(num2))
        first_int()
    if sym == "/":
        print(float(org) / float(num2))
        first_int()
first_int()
