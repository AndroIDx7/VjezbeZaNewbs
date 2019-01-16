#break and cotinue statements, and else clauses on loops
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break

for num in range(2,10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found a number", num)

'''
#Pass statements
class MyEmptyClass:
    pass
def initlog(*args)
    pass

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

fib(2000)



def fib(n):
    a,b = 0, 1
    while a<n:
        print(a, end= ' ')
        a, b = b, a+b
        print()
fib(2000)


friends = ["Mihael", "Samuel", "Lubo"]
for index in range(5):
    if index == 0:
        print("First Iteration")
    else:
        print("not first")


a = min([sum([11, 22]),max(abs(-30),2)])
print(a)


#EXPONENT FUNCTION

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(3, 4))


#2D LISTS AND NESTED LOOPS

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[2][1])

for row in number_grid:
    for col in row:
        print(col)

#BUILD A TRANSLATOR


def translate(phrase):
    translation = " "
    for letter in phrase:
        if letter.lower() in "aeiou":
            translation = translation + "g"
        else:
            translation = translation + "G"
    return translaion

print(translate(input("Enter a phrase: "))
'''

'''
def simple(num1, num2):
    pass
def simple(num1,num2=5):
    print(num1,num2)

def basic_window(width, height, font = 'TNR',
                 bgc='w', scrollbar=True):
    print(width,height,font,bgc)

basic_window(500,350,bgc='b')
'''

#Functional programming from SoloLearn
def apply_twice(func, arg):
    return func(func(arg))

def add_five(x):
    return x + 5
print(apply_twice(add_five, 10))

def test(func, arg):
    return func(func(arg))

def mult(x):
    return x*x

print(test(mult, 2))

#pure functions

def pure_function(x, y):
    temp = x + 2*y
    return temp / (2*x + y)

some_list = []

def impure(arg):
    some_list.append(arg)


#named functions
def polynomial(x):
    return x**2 + 5*x + 4
print(polynomial(-4))

#lambda
print((lambda x: x**5 + 5*x + 4)
(-4))

print('DOESN\'T')

print('py''thon')


#multiply each item by 2 using lambda sytax
nums = [11, 22, 33]
a = list(map(lambda x: x*2, nums))
print(a)

numeri = [1,2,3,4,5,6,0,7]
res = list(filter(lambda x: x < 5, numeri))
print(res)










