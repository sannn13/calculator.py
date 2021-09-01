#!/usr/bin/env python
# coding: utf-8

# In[ ]:


while True:
    number_1 = int(input("Enter first operand: "))
    number_2 = int(input("Enter second operand: "))
    operation = input("Enter an operator (+,-,*,/): ")


    def add(a, b):
        print("Sum of", a, "&", b, "is: ", a + b)


    def sub(a, b):
        print("Difference of", a, "&", b, "is: ", a - b)


    def mult(a, b):
        print("Multiplication of", a, "&", b, "is: ", a * b)


    def divide(a, b):
        print("Division of", a, "&", b, "is: ", a / b)


    def result(a, b, op):
        if op == '+':
            add(a, b)
        elif op == '-':
            sub(a, b)
        elif op == '*':
            mult(a, b)
        elif op == '/':
            divide(a, b)
        else:
            print("Invalid Entry ")


    result(number_1, number_2, operation)
    loop = input("Enter N to exit. Press any other key to continue ")
    if loop.upper() == 'N':

        break
    else:
        print(" ")


# ## 
