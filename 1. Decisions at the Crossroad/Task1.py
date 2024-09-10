#Task 1: Code Correction You are provided with a 
# Python script that uses conditional statements 
# to tell if a number is positive, negative, 
# or zero, but it has some errors. 
# Identify and fix them.

number = input("Enter a number: ")

if number > "0":
    # " " missing around 0 is line 9 and 12. Variable is an input
    # of an str, "0", and cannot be compared to an int, 0.
    print("The number is positive.")
elif number == "0": # "=" implies assignment "==" is an operator,
    # an operator is needed in this scenario.
    print("The number is zero.")
else: # "number < 0" is not needed because else will
    # run when if & elif return False. 
    # If number is not > or == 0, it can only be < 0.
    print("The number is negative.")