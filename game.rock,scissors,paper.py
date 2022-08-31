from random import randint

from requests import options

def win():
    print ('You win!')

def lose():
    print ('You lose!')

while True:
    player_choice = input('What do you pick? (rock, paper, scissors)')
    player_choice.strip()
    random_move = randint(0, 2)
    moves = ['rock', 'paper', 'scissors']
    option= ['paper', 'scissors', 'rock']
    computer_choice=option[random_move]
    if player_choice==computer_choice:
        print ('Draw!')
    elif player_choice=='rock' and computer_choice == 'scissors':
        win()
    elif player_choice== 'paper' and computer_choice == 'scissors':
        lose()
    elif player_choice == 'scissors' and computer_choice == 'paper':
        win()
    elif player_choice == 'scissors' and computer_choice == 'rock':
        lose()
    elif player_choice == 'paper' and computer_choice == 'rock':
        win()
    elif player_choice== 'rock' and computer_choice  == 'paper':
        lose()
        
    again = input('Do you want to play again? (y or n)')
    if again == "y":
        print("start game again")
    elif again=="n":
        print("thank you")
        break


player=input("what you pick")
computer=input("what you pick")
if player==computer:
        print ('Draw!')
elif player=='rock' and computer == 'scissors':
    print("win")
elif player== 'paper' and computer == 'scissors':
    print("lose")
elif player== 'scissors' and computer == 'paper':
    print("win")
elif player == 'scissors' and computer == 'rock':
    print("lose")
elif player == 'paper' and computer == 'rock':
    print("win")
elif player== 'rock' and computer  == 'paper':
    print("lose")
        
again = input('Do you want to play again? (y or n)')
if again == "y":
    print("start game again")
elif again=="n":
    print("thank you")
# break


 