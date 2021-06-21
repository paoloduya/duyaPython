import random

firstNumber = random.randint(0, 10)
secondNumber = random.randint(0, 10)

print("First Number :" + str(firstNumber))
print("Second Number:" + str(secondNumber))

print("")
print("OPERATION:")
print("A: Addition")
print("B: Subtraction")
print("C: Multiplication")
print("D: Division")
print("")

operator = input("Choose Operation:")

if operator == 'A' or operator == 'a':
    total = firstNumber + secondNumber
    my_Answer = int(input("What is your answer?"))
    if total == my_Answer:
        print("Great you got the right answer!")
    else:
        print("Wrong, the correct answer is: " + str(total))

elif operator == 'B' or operator == 'b':
    total = firstNumber + secondNumber
    my_Answer = int(input("What is your answer?"))
    if total == my_Answer:
        print("Great you got the right answer!")
    else:
        print("Wrong, the correct answer is: " + str(total))
elif operator == 'C' or operator == 'c':
    total = firstNumber + secondNumber
    my_Answer = int(input("What is your answer?"))
    if total == my_Answer:
        print("Great you got the right answer!")
    else:
        print("Wrong, the correct answer is: " + str(total))

elif operator == 'D' or operator == 'd':
    total = firstNumber + secondNumber
    my_Answer = int(input("What is your answer?"))
    if total == my_Answer:
        print("Great you got the right answer!")
    else:
        print("Wrong, the correct answer is: " + str(total))