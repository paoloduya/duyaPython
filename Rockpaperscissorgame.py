import random

player_Score = 0
computer_Score = 0
while True:

    choices = ['rock', 'paper', 'scissors']
    computer = random.choice(choices)

    player = str(input('Choose Rock, Paper ,Scissors:')).strip().lower()
    print()

    if player == 'rock' and computer == 'scissors' or \
       player == 'scissors' and computer == 'paper' or \
       player == 'paper' and computer == 'rock':

        print(f'You choose {player}. the computer choose {computer}. YOU WIN!')
        player_Score = player_Score + 1

    elif player == 'rock' and computer == 'paper' or \
        player == 'scissors' and computer == 'rock' or \
            player == 'paper' and computer == 'scissor':

        print(f'You choose {player}. the computer choose {computer}. YOU LOSE!')
        computer_Score = computer_Score + 1

    else:
        if player == computer:
            print(f'You choose {player}. the computer choose {computer}. Its a tie!')
            player_Score = player_Score + 1
            computer_Score = computer_Score + 1

    print()
    print("Player Score:" + str(player_Score))
    print("Computer Score:" + str(computer_Score))
    print("")
    repeat = input("Do you want to play again? Yes/No: ")
    print("_________________________________________________________")

    if repeat.lower() == "y":
        pass
    else:
        print("thank you for playing")
        break