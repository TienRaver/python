import random
def getchoice():
    computer_list = ["Rock", "Paper", "Scissor"] # Khai bao list chon cua computer
    player_choice = input("Enter your choice (Rock/Paper/Scissor): ")
    computer_choice = random.choice(computer_list) # May tinh lua chon ngau nhien
    choice = {"player": player_choice, "computer": computer_choice}
    return choice
def check_win(player,computer):
    print(f"You chose: {player}, computer chose: {computer}")
    if player == computer:
        print("It's a tie!")
    elif player == "rock":
        if computer == "scissor":
            print("You win!")
        else:
            print("You lose.")
    elif player == "paper":
        if computer == "scissor":
            print("You lose.")
        else:
            print("You win")
check_win("rock","paper")
