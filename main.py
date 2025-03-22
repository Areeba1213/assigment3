# control flow and loops in pythone
# Control flow refers to the way we control the execution of our program. It includes if-else statements and loops.

# IF-ELSE STATMENT
# This is used to check conditions and execute code accordingly.
# EXAMPLE
age = 15
if age >= 15:
  print("you are allowed for this ride")
else:
  print("you are not allowed for this ride")
#    If age is 15 or more, the if block will execute; otherwise, the else block will run.
# LOOPS
# Loops are used to execute a block of code multiple times until a condition is met. There are two types of loops in Python:
# For Loop, While Loop
# FOR LOOP If we need to iterate over a list or a range, we use a for loop.
for i in range(6):
 print("Hello world!") 
#  This loop will print "Hello, World!" six times (from 0 to 6).
# If we want to iterate over a list or tuple
fruits = ["Guava" , "Mango","Papaya"]
for fruit in fruits:
   print(fruit)
#    This will print each item in the list one by one.
# WHILE LOOP
# A while loop keeps running as long as the condition is True.
count = 1
while count <= 6:
   print("Count:" ,count) 
   count += 1
#    This loop will run six times and print the count.Be careful with infinite loops! Always make sure the condition eventually becomes False, or the loop will never stop. 
#   Loop Control Statements
# break → Immediately stops the loop.
# continue → Skips the current iteration but continues the loop.
# pass → Does nothing, just a placeholder.
# Break Example
for num in range(10):
  if num == 5:
    break
  print(num)
#   This loop will run only from 0 to 4, because it breaks at 5.
#  Continue Example
  for num in range(5):
   if num == 3:
     continue
  print(num) 
#   Lists, Tuples, and Dictionaries
# List: A mutable (changeable) collection written inside square brackets []
thislist = ["apple", "banana", "cherry"]
print(thislist)
# Changeable (can add/remove items),Ordered (maintains sequence),Allows duplicate values
# Tuple : An immutable (unchangeable) collection written inside round brackets ()
#  Tuple as a Data Structure Tuples (tuple) are immutable sequences used to store multiple values
my_tuple = (1, 2, 3, "apple")
#  Tuple as a Return Type Functions in Python can return multiple values as a tuple.
def get_coordinates():
    return (10.5, 20.3)  # Returns a tuple

x, y = get_coordinates()
#  Tuple for Dictionary Keys Since tuples are immutable, they can be used as dictionary keys (lists cannot).
my_dict = {(1, 2): "Point A", (3, 4): "Point B"}
# 4. Tuple Unpacking You can unpack tuples easily.
person = ("Ali", 25, "Pakistan")
name, age, country = person
print(name, age, country)  # Ali 25 Pakistan
#  Tuple as a Named Tuple Python’s collections.namedtuple allows readable field names in tuples.
from collections import namedtuple
Person = namedtuple("Person", ["name", "age"])
p1 = Person("Ali", 25)
print(p1.name, p1.age)
# 6. Tuple as a Type Hint in Python When writing functions, you can use tuples in type hints.
def get_data() -> tuple[str, int]:  # Tuple with str and int
    return ("Ali", 25)
# Dictionary → A collection of key-value pairs written inside curly brackets {}.
student = {"name": "Ali", "age": 20, "city": "Lahore"}
student["age"] = 21  # Values in a dictionary can be updated
# Keys are unique,Changeable (can update values),Ordered (maintains order from Python 3.7+)

# Set vs Frozen Set in Python Set → Mutable (Can be changed)we can add or remove elements,Written as {1, 2, 3}.
my_set = {1, 2, 3}
my_set.add(4)  # You can add elements
my_set.remove(2)  # You can remove elements
print(my_set)  # Output: {1, 3, 4}

# Frozen Set → Immutable (Cannot be changed)Once created, it cannot be modified,Written as frozenset({1, 2, 3}).
my_fset = frozenset({1, 2, 3})
my_fset.add(4)  # This will give an error because it cannot be changed
print(my_fset)  # Output: frozenset({1, 2, 3})
# If you want to protect your data from accidental changes, use a frozenset
