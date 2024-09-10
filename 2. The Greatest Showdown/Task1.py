# Identify the Greatest Write a Python program that
# asks the user to enter three numbers. 
# Your code should then identify and print out the 
# largest number among the three.

print("Pick any three numbers!")
number1 = int(input())
number2 = int(input())
number3 = int(input())

if number1 > number2 and number1 > number3:
    print(number1, "is the largest of the group")
elif number2 > number1 and number2 > number3:
    print(number2, "is the largest of the bunch!")
else:
    print(number3, "takes the cake")
