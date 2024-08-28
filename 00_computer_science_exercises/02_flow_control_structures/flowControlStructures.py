# Flow Control Structures, Andrew Patton, v0.0
# Making Computer Programs Make Decisions

temperature = 56.78
color = "Blue"
height = 7
likesPineapplesOnPizza = False

# SINGLE DECISION POINT - if Statement
# if CONDITIONAL_EXPRESSION: <-- This will use a COMPARISON OPERATOR 99% of the time.
    # runThisCode IF the CONDITIONAL_EXPRESSION is True

if temperature > 100:
    print("It is hot as the sun outside.\n")

if color == "Blue":
    print("The sky is blue.\n")

# CHEAT CODE FOR IF STATEMENTS THAT USE BOOLEANS.
if likesPineapplesOnPizza:
    print("Gross")

# What if we want something different to happened?
if color == "Red": # COMMON ERROR FOR STUDENTS IS USING = instead of ==.
    print("Your shirt is the correct uniform color.\n")
else:
    print("Your shirt is not the correct uniform color\n")

if height == 7:
    print("Your tall enough to get on the ride")
else:
    print("Your are not tall enough to get on the ride")