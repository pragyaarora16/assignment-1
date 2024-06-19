num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
str1 = input("Enter the operator")
if str1 == '+':
    result = num1+num2
elif str1 == '-':
    result = num1-num2
elif str1 == '*':
    result = num1*num2
elif str1 == '/':
    result = num1//num2
print("Result:", result)
