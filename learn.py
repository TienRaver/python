# Chuong trinh choi OAN TU TI voi may tinh
# Nhap thu vien ngau nhien
import random
# Tao func getchoice() va check_win()
def getchoice():
    computer_list = ["rock", "paper", "scissor"] # Khai bao list chon cua computer
    computer_choice = random.choice(computer_list) # May tinh chon ngau nhien tu computer_list
    player_choice = input("Enter your choice (rock/paper/scissor): ") # Nhap lua chon cua nguoi choi
    choice = {"player": player_choice, "computer": computer_choice} # Gan dict choice
    return choice # Tra ve choice
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
    else:
        if computer == "paper":
            print("You win!")
        else:
            print("You lose.")
choices = getchoice() # Goi func getchoice va gan bien choices
result = check_win(choices["player"],choices["computer"]) # Goi func check_win va truyen bien tu choices
print(result)