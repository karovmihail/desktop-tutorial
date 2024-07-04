import random
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))
player_score = 0
computer_score = 0
while(True):
    rock = "Rock"
    paper = "Paper"
    scissors = "Scissors"
    player_move = input("Choose [r]rock, [p]paper, [s]scissors: ")
    if player_move == "r":
        player_move = rock
        prLightPurple("You chose rock.")
    elif player_move == "p":
        player_move = paper
        prLightGray("You chose paper.")
    elif player_move == "s":
        player_move = scissors
        prLightGray("You chose scissors.")
    else:
        raise SystemExit("Invalid Input. Try again...")
    computer_move = ""
    computer_random_number = random.randint(1,3)
    if computer_random_number == 1:
        computer_move = rock
        prPurple("The computer chose rock.")
    elif computer_random_number == 2:
        computer_move = paper
        prRed("The computer chose paper.")
    else:
        computer_move = scissors
        prGreen("The computer chose scissors.")
    if (player_move == rock and computer_move == scissors) or \
        (player_move == paper and computer_move == rock) or \
        (player_move == scissors and computer_move == paper):
        player_score += 1
        prCyan("You win!!! :)")
    elif player_move == computer_move:
        prYellow("Draw! :|")
    else:
        computer_score += 1
        prBlack("You lose! :(")
    prLightGray(f"Current score You - {player_score}, Computer - {computer_score}")
    play_again = input("Type [yes] to Play Again or [no] to quit: ")
    if play_again == "yes":
        prCyan(player_move)
        break
    if play_again == "no":
        prRed("Thank you for playing!")
        break
