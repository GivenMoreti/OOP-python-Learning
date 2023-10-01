height = 120
print("Your height is " + str(height))
print(type(str(height)))
name = "Given23"
print("-" * 10)
print(name.isalpha())
print(name.isalnum())

# typecasting
print("type casting starts here")
print("-" * 10)
print(type(height))
height = float(height)
print(type(height))
print(height)
height = str(height)
print(type(height))
print(height)

# slicing
# [start:stop:step]

print("-" * 10)
print('slicing')
name = "Given Moreti"
first_name = name[0:5]
print("First name is " + first_name)
surname = name[6:]
print("Surname is " + surname)
# apply stepping
funky_name = name[0:5:2]  # Gvn
funky_name = name[::2]  # Giv
print(funky_name)  # GvnMrt take every second letter

# reverse a string
reversed_name = name[::-1]
print(reversed_name)  # iteroM neviG

# lists -mutable and store non-related data
food = ["tea", "bread", "pap"]
# returns ["tea","bread","pap"] unlike c++ which returns food[0] only
print(food)
# food[10] = "Mayo"       #returns error


# to print the elements using for loop
for i in food:
    print(i)
    # returns tea bread pap on a new line
# CRUD
# appending
food.append("Mayo")
print(food)
# removing
food.remove("bread")
print(food)
# inserting
food.insert(0, "guava")
print(food)
# sorting
food.sort()  # alphabetical
print(food)
# cextend the food array
drinks = ["foo", "fee", 10]
food.extend(drinks)
print(food)
food.clear()
print(food)

# 2 -d lists - is a list of lists
drinks = [1, "beer", "juice", "coffee"]
main = ["pap", "beans", "rice"]
dessert = ["ice cream", "mayo"]

food = [drinks, main, dessert]
# [[1, 'beer', 'juice', 'coffee'], ['pap', 'beans', 'rice'], ['ice cream', 'mayo']]
print(food)
# list drinks [0],main[1],dessert[2]
print(food[0])
print(food[1])
print(food[2])
# to access individual elements food[][]
print(food[0][1])  # beer

# tuple = immutable and store related data
student = ("Given", "moreti", 23)
print(student.count("Given"))
# iterating through a list
for i in student:
    print(i)

# sets - unordered , unindexed and non duplicated

gadgets = {"Phone", "Laptop", "computer"}

print(gadgets)  # {'Laptop', 'computer', 'Phone'}
gadgets.add("mouse")
print(gadgets)
gadgets.pop()
print(gadgets)
# ideal in randomized data to shuffle outcome

# dictionaries - mutable,unordered, key:value pairs ,fast because they use hashing
capitals = {'usa': "WDC",
            "india": "new delhi",
            "sa": "pta"
            }

print(capitals["india"])
# prevents program breaking when searching for non existing key
print(capitals.get("limpopo"))
capitals.update({"Sa": "Limpopo"})
print(capitals)

print("*" * 10)
print("index operator []")
name = "mike"

if (name[0].islower()):  # check if the first element  in name is lower
    name = name.capitalize()
    print(name)

name = name[:].upper()  # [:] means all the elements
print(name)

# functions using keyword arguments


def greet(first, middle, last):

    print("Hello " + first + " " + middle + " " + last)


# implement the keywords to retain order
greet(middle="tlou", last="Moreti", first="Given")

# nested functions
# print(round(abs(float(input("Enter a decimal number ")))))
# return functions


def add(*my_args):      # first convert the arguments into a tupple
    sum = 0
    for i in my_args:
        sum += i
    return sum


total = add(3, 4, 6, 8, 9, 0, 7, 5, 6, 7, 8)
# print(total)

# to convert to a list


def add(*args):
    sum = 0
    another = list(args)
    another[2] = 23
    for i in another:
        sum += i
    return sum
# print(add(2,4,5))   #replaces the element[2] with 23 then sum.
