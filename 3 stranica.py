'''
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = float(num1) + float(num2)
print(result)


#if, elif else aaaaan return kao rezultat:
def max_num(num1, num2, num3 ):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
print(max_num(300, 40, 5))
'''


#Kalkulator

num1 = float(input("Enter first number: "))
Op = input("Enter Operator: ")
num2 = float(input("Enter second number: "))

if Op == "+":
    print(num1 + num2)
elif Op == "-":
    print(num1 - num2)
elif Op == "*":
    print(num1 * num2)
elif Op == "/":
    print(num1 / num2)
else:
    print("Invalid operator")

#krivo si upisao num2, zamjenio si sa num1, pazi na duple zagrade.
'''
username = 'dre'
password = 'javisestari'


print("Welcome to my page")
input("Enter username: ")
input("Enter password: ")

if username and password is  True:
    print("logged in")
else:
    print("input incorrect")
    
'''
