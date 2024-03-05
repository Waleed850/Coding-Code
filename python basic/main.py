"""def say_hello(name, age):
    print("His name is " + name + " and he is " + age)

say_hello("waleed", "25")

def cube(num):
    return num * num * num

print(cube(3))

def cube():
    return 4 * 4 * 4

print(cube())

is_pass = True
is_fail = False
if is_pass or is_fail:
    print("they should be promoted")
else:
    print("they should be stuck out")"""

"""num = 2
for i in range(1, 11):
    print(num, 'x', i, '=', num*i)

num = int(input("Table of ? "))
for i in range(1, 11):
    print(num, 'x', i, '=' , num*i)"""

# Task 1
"""num = 2
for i in range(1, 11):
    print(num, 'x', i, '=', num*i)
#Task 2
num = int(input("Multiplication table of: "))
for i in range(1, 11):
    print(num, 'x', i, '=', num*i)"""


##########################################
# def function
"""def say_hello(name, age):
    print("His name is " + name + " and he is " + age)


say_hello("waleed", "25")


# Def return statement
def cube(num):
    return num * num * num


print(4)


def cube():
    return 3 * 3 * 3 * 3


print(cube())"""
##########################################
# Better calculator
"""num1 = float(input("Enter the first number: "))
op = input("Select the operator: ")
num2 = float(input("Enter the second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("invalid operator")"""
#############################
# While loops
"""i = 1
while i <= 10:
    print(i)
    i += 1
print("Done")"""

############################
# For loops
"""for number in range(10):
    print(number)

friends = ["Awaits", "Raza", "Ahmad"]
for friend in friends:
    print(friend)"""
############################
# nested loop is the loop inside the loop
"""number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
for row in number_grid:
    print(row)

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
for row in number_grid:
    for col in row:
        print(col)"""

##############################
# Multiplication table of 1 to 10


"""for i in range(2, 11):
    num = int(input("Multiplication table of: "))
    print("\nTable %d\n" % i)
    for j in range(2, 11):
        print("\n%-5d X %5d = %5d" % (i, j, i * j), end=' ')"""

# list: ordered, allow duplicate elements
"""mylist = ["banana", "cherry", "apple"]
print(mylist)

if "banana" in mylist:
    print("yes")
else:
    print("no")"""

"""mylist = ["banana", "cherry", "apple"]
print(mylist)
mylist.append("banana") # also remove, pop
print(mylist)

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(mylist[1:6])"""

"""mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
a = [x*x for x in mylist] #important

print(mylist)
print(a)"""

# Tuples: ordered, unchangeable allows duplicate element

"""tuple_list = tuple(["Car", "Heavy-bike", "Motor Bike"])
print(tuple_list)

for i in tuple_list:
    print(i)"""

# Dictionaries
"""mydict = {"Name": "Waleed", "Age": 23, "City": "Rawalpindi"}
print(mydict)

try:
    print(mydict["lastname"])
except:
    print("Error")

for i in mydict:
    print(i)"""

# strings: ordered, immutable text representation
"""my_string = "I am a programmer"
char = my_string[5]
print(char)

my_string = "I am a programmer"
my_list = my_string.split()
print(my_list)"""

# string, int formatter %s for string, %d for decimal

"""var = "Waleed"
my_list = "The variable is %s" % var
print(my_list)

var = 20
my_list = "The variable is %d" % var
print(my_list)

var = 20.345
my_list = "The variable is %f" % var
print(my_list)

var = 20.567
my_list = f"The variable is {var}"
print(my_list)"""

#Madlibs project
Adj = input("Your Adjective: ")
verb = input("Your verb: ")
person = input("Famous Person: ")
madlibs = f"Computer Programming is {Adj}! As it is {verb}! Like famous programmer and youtuber {person}!"
print(madlibs)














