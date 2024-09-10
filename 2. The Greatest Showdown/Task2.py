# Task 2: Identify the Smallest Improve upon your code
# from Task 1 to also determine the smallest number 
# among the three and print it out.

print("Pick any three numbers!")
number1 = int(input())
number2 = int(input())
number3 = int(input())

if number1 > number2 and number1 > number3 and number2 > number3:
    print(number1, "is the largets of the group, and", number3, "is the smallest.")
elif number1 > number2 and number1 > number3 and number3 > number2:
    print(number1, "is the largets of the group, and", number2, "is the smallest.")
elif number2 > number3 and number2 > number1 and number1 > number3:
    print(number2, "is the largets of the group, and", number3, "is the smallest.")
elif number2 > number3 and number2 > number1 and number3 > number1:
    print(number2, "is the largets of the group, and", number1, "is the smallest.")
elif number3 > number2 and number3 > number1 and number2 > number1:
    print(number3, "is the largets of the group, and", number1, "is the smallest.")
else:
    print(number3, "is the largets of the group, and", number2, "is the smallest.")
