numbers = [1,2,3]
strings = ["Hello", "World"]
names = ["John", "Eric", "Jessica"]
#write your code here
numbers.append(1)
numbers.append(2)
numbers.append(3)

strings.append("hello")
strings.append("world")

second_name = names[1]
print("The second name on the list is %s" % second_name)



number = 1 + 2 * 3 / 4
print(number)

remainder = 11 % 3
print(remainder)

squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)

helloworld = "hello" + " " + "world"
print(helloworld)

lotsofhellos = "hello" * 10
print(lotsofhellos)

even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7,9]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

print([1,2,3] * 3)

x = object()
y = object()

#TODO: change this code
x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" %len(big_list))

#testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!!")

coordinates = [(4, 5), (6,7), (80,34)]
coordinates[1] = 10
print(coordinates[1])

def say_hi(name, age):
    print("Hello " + name + "you are " + str(age))

say_hi("Mike", 35)
say_hi("Steve", 11)


#IF STATEMENTS


is_male = True
is_tall = True

if is_male or is_tall:  #OR!!
    print("You are a male or tall or both")
else:   #Otherwise..
    print("You neither male nor tall")


is_male = True
is_tall = True

if is_male and is_tall: #AND!!
    Print("You are a tall male")
elif is_male and not is_tall:
    print("you are not a male but are tall")
elif not(is_male) and is_tall:
    print("You are not a male but are tall")
else:
    print("You are either not male or not tall or both")



def max_num(num1, num2, num3 ):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
print(max_num(3, 4, 5))