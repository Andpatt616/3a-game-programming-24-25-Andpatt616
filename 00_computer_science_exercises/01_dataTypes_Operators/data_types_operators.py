# Data Types and Operators, Andrew Patton, v0.0

# Fundamental Data Types
# String - str - Sequence of letter, numbers, spaces, or other characters.
# Strings in Python are inside ' ' or " "
# idc if you use ' ' or " " just be consistent.

# Boolean - bool - True or False values.

# Float - float - any number with a decimal, +/-, including 0.0.

# Integers - int - any whole numbers, +/-, including 0.

# Data types are stored in VARIABLES.
# A variable is basically a bucket with a name to put data into.
# VARIABLE NAMES SHOULD TELL YOU WHAT DATA IS BEING STORED IN IT.
# VARIABLES CANNOT START WITH A NUMBER
# camelCaseVariableNames
# snake_case_variable_names

# DECLARING VARIABLES AND ASSIGNING VALUES

high_score = 83745512 # int data types
highScore = 304872612 # int data types

carSpeed = 123.2341 # float data type, miles per hour
car_speed = 5.29342 # float data type, miles per hour

hasAxe = True # boolean data type
isPurple = False # boolean data type

playerName = "Andrew Patton" # string data type
player_dialoge = "Hello there" # string data type

# ASSIGN NEW VALUES
playerName = "Paul goodman"
car_speed = 2.34

# DATA TYPES CAN CHANGE, BE CAREFUL
hasAxe = 3.67

# printing Variables to Console / Screen
print(high_score)
print(car_speed)
print(hasAxe)
print(player_dialoge)

# printing variables and expressions to console / screen
print(high_score + 5024)
print(26 * 254)
print(high_score)


# PRINTING VARIABLES INSIDE OF STRINGS
print(f"Hello {playerName}. Your new high score is {highScore}.\n")

# ARITHMETIC OPERATORS
myInt = 4
myFloat = 3.75
myNum = 0

#addition
myInt = 9 + 2
myFloat = 9.75 + 2.0

myInt = myInt + 5

myNum = myInt + myFloat
# When you add an Int and a float together, the answer becomes a float

# subtraction
myNum = myInt - myFloat
myInt = myFloat - 1.25

# Multiplication
myNum = myInt * myFloat

# Division
myNumber = myInt / myFloat # first is numerator, second num is denominator