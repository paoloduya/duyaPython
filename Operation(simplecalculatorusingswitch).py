import random

true = 0
false = 0
while True:
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
            true = true + 1
        else:
            print("Wrong, the correct answer is: "+str(total))
            false = false + 1

    elif operator == 'B' or operator == 'b':
        total = firstNumber + secondNumber
        my_Answer = int(input("What is your answer?"))
        if total == my_Answer:
            print("Great you got the right answer!")
            true = true + 1
        else:
            print("Wrong, the correct answer is: "+str(total))
            false = false + 1
    elif operator == 'C' or operator == 'c':
        total = firstNumber + secondNumber
        my_Answer = int(input("What is your answer?"))
        if total == my_Answer:
            print("Great you got the right answer!")
            true = true + 1
        else:
            print("Wrong, the correct answer is: "+str(total))
            false = false + 1

    elif operator == 'D' or operator == 'd':
        total = firstNumber + secondNumber
        my_Answer = int(input("What is your answer?"))
        if total == my_Answer:
            print("Great you got the right answer!")
            true = true + 1
        else:
            print("Wrong, the correct answer is: "+str(total))
            false = false + 1
    print("")
    print("Correct Answer:"+str(true))
    print("Wrong Answer:"+str(false))
    print("")
    repeat = input("Do you want to play again? Yes/No: ")
    print("")
    print('--------------------------------------------------------')

    if repeat.lower() == "y":
        pass
    else:
        print("thank you for playing")
        break