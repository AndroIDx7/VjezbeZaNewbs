'''# Fibonacci series:

# the sum of two elements defines the next
a,b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a+b

i = 256*256
print("The value of i is", i)

x = int(input("Please enter an interger: "))
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print("zero")
elif x == 1:
    print("single")
else:
    print("more")


#Measure some strings:
words = ["Kira", "Kaku", "Valfiorita", "Nadija", "Ariana"]
for w in words[:]:
    if len(w) > 6:
        words.insert(0, w)


for w in words[:]:  #loo over a slice copy of the entire list.
    if len(w) > 6:
        words.insert(2, w)
'''
'''
# Range() functions:
for i in range(5):
    print(i)

for b in range(3,12):   #primjer 1
    print(b)

for n in range(-10, -100, -20):     #primjer 2
    print(n)

for h in range(0, 15, 5):   #primjer 3
    print(h)
'''
'''
a = ["Andre", 'Ari', 'Boba', 'Silvo', 'lamb']
for i in range(len(a)):
    print(i, a[i])

#Def i return
def cube(num):
    return num*num*num
result = cube(4)
print(result)



#Dictionaries
monthConversion = {
    "Jan": "January",    #Key and Values
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
}

print(monthConversion.get("Apr"))   #kad ide .get ne idu []
print(monthConversion["Jan"])



#While loops

i = 1
while i <=10:
    print(i)
    i = i + 1   #ili mos i+=1

print("Done with loop")
'''
#Building a Guessing game

secret_word = "blockchain"
guess = ""  #Variables
guess_count = 0
guess_limit = 5
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("no mo guessin!")
else:
    print("Got it Bitch")




















