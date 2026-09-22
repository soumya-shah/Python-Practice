# defining a function:
def my_function(name):
    print("hello my name is ",name)  
# here name is a parameter
my_function("emily")
# here emily is argument 

def my_function(fname, lname):
  print(fname + " " + lname)
# this function expects 2 arguments so if we will give 1 it will throw an error

my_function("Emil", "Refsnes")

# we can keep default value for a parameter so that if no argment is passed we can use this. 
def my_function(name = "friend"):
  print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus")

# keyword arguments: 
# You can send arguments with the key = value syntax.
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(name = "Buddy", animal = "dog")

# To specify that a function can have only keyword arguments, add *, before the arguments:
def my_function(*, name):
  print("Hello", name)

my_function(name = "Emil")

# combining both:
def my_function(a, b, /, *, c, d):
  return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result)


# This way, with keyword arguments, the order of the arguments does not matter.

# Positional arguments:
# When you call a function with arguments without using keywords, they are called positional arguments.
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)
my_function("dog", "Buddy")

#  we can also specify to a function thta if he can has only positional arguments.
def my_function(name, /): 
#  by using a /
  print("Hello", name)

my_function("Emil")




# we can send any data type as arguments in a function string list dict tuple
def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)

def my_function(person):
  print("Name:", person["name"])
  print("Age:", person["age"])

my_person = {"name": "Emil", "age": 25}
my_function(my_person)

#  function can return values using return statement 
def my_function(x, y):
  return x + y

result = my_function(5, 3)
print(result)

# args and kwargs
# *args and **kwargs allow functions to accept a unknown number of arguments.
#  args store as tuple and kwargs as dictionary


# ARBITARY ARGUMENTS:(*args)
# if you do not know how many arguments will be passed into your function, add a * before the parameter name.
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")


# if we dont specify teh position to be used 
def my_function(greeting, *names):
  for name in names:
    print(greeting, name)

my_function("Hello", "Emil", "Tobias", "Linus")

# Arbitrary Keyword Arguments - **kwargs
# the function will receive a dictionary of arguments and can access the items accordingly:
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

def my_function(username, **details):
  print("Username:", username)
  print("Additional details:")
  for key, value in details.items():
    print(" ", key + ":", value)

my_function("emil123", age = 25, city = "Oslo", hobby = "coding")

# args and kwargs: 
# You can use both *args and **kwargs in the same function.

# The order must be:

# regular parameters
# *args
# **kwargs

def my_function(title, *args, **kwargs):
  print("Title:", title)
  print("Positional arguments:", args)
  print("Keyword arguments:", kwargs)

my_function("User Info", "Emil", "Tobias", age = 25, city = "Oslo")

# Unpacking Arguments
# The * and ** operators can also be used when calling functions to unpack (expand) a list or dictionary into separate arguments.
def my_function(a, b, c):
  return a + b + c

numbers = [1, 2, 3]
result = my_function(*numbers) # Same as: my_function(1, 2, 3)
print(result)

def my_function(fname, lname):
  print("Hello", fname, lname)

person = {"fname": "Emil", "lname": "Refsnes"}
my_function(**person) # Same as: my_function(fname="Emil", lname="Refsnes")

# PYTHON DECORATORS:
# A decorator is a function that takes another function as input and returns a new function.

def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

print(myfunction())

def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

@changecase
def otherfunction():
  return "I am speed!"

print(myfunction())
print(otherfunction())

def changecase(func):
  def myinner(x):
    return func(x).upper()
  return myinner

@changecase
def myfunction(nam):
  return "Hello " + nam

print(myfunction("John"))

# PYTHON LAMBDA
# A lambda function can take any number of arguments, but can only have one expression.

# RECURSION
# Recursion is when a function calls itself.
# Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.

def countdown(n):
  if n <= 0:
    print("Done!")
  else:
    print(n)
    countdown(n - 1)

countdown(5)

# Every recursive function must have two parts:

# A base case - A condition that stops the recursion
# A recursive case - The function calling itself with a modified argument
def factorial(n):
  # Base case
  if n == 0 or n == 1:
    return 1
  # Recursive case
  else:
    return n * factorial(n - 1)

print(factorial(5))

# FIBONACCI SEQUENCE 
def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(5))


# recursion with lists
def sum_list(numbers):
  if len(numbers) == 0:
    return 0
  else:
    return numbers[0] + sum_list(numbers[1:])

my_list = [1, 2, 3, 4, 5]
print(sum_list(my_list))

# find maximum value in lists:
def max_value(numbers):
  if len(numbers)==1:
    return numbers[0]
  else:
    max_of_rest = max_value(numbers[1:])
    return numbers[0] if numbers[0] > max_of_rest else max_of_rest
    

my_list = [3, 7, 2, 9, 1]
print(max_value(my_list))

# Recursion Depth Limit
# Python has a limit on how deep recursion can go. The default limit is usually around 1000 recursive calls.
