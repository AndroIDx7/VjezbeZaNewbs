#this prints out john is 23 years old
'''
name = "John"
age = 23
print("%s is %d years old." % (name, age))

#this prints out A list: [1,2,3]
mylist = [1, 2, 3]
print("A list: %s" % mylist)

myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)

mystring = "hello"
print(mystring)
mystring = "hello"
print(mystring)

one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)



#this prints out Hello John Doe. Your current balance is $53.44
data = ("John", "Doe", 53.44)
format_string = "Hello %d. Your current balance is %s"

# change this code
mystring = "hello"
myfloat = 10.0
myint = 20

if mystring == "hello":
    print("String: %s" % mystring)
if myfloat == 10.0:
    print("Float: %f" % myfloat)
if myint == 20:
    print("Integrer: %d" % myint)

mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0]) #prints 1
print(mylist[1]) #prints 2
print(mylist[2]) #prints 3

#prints out 1,2,3
for x in milist:
    print(x)


milist = [1,2,3,4,5,6,7]
print(milist[50])
'''
#Comments are used for me so I can understand something

#TRY EXCEPTION

try:
    value = 10 / 0
    number = int(input("Enter a number: "))
    print(number)   #Integer = int - pita za unos broja.
except ZeroDivisionError as err:   #Except dodajemo kako bi predvidjeli nekakavb output
    print(err)
except ValueError:
    print("Invalid input")

#READING FILES (OUSIDE FILES)


from itertools import count
for i in count(3,2):
    print(i)
    if i>=11:
        break

from itertools import product
a={1, 2}
print(len(list(product(range(3), a))))

def power(x, y):
    if y == 0:
        return 1
    else:
        return x* power(x,y-1)

print(power(2, 3))