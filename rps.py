choicels = ['rock','paper','scissors','lizard','spock']

import random

computer = random.choice(choicels)
user = input("'Please choose betweeen, 'rock','paper','scissors','lizard','spock'?: ").lower()


while user not in choicels:
    user = input("'Choice does not exist, Please choose betweeen, 'rock','paper','scissors','lizard','spock'?: ").lower()
    
else:
    if user == computer:
        print('Draw')
    elif user == 'rock' and computer == 'scissors':
        print('User Won')
    elif user == 'scissors' and computer == 'paper':
        print('User Won')
    elif user == 'paper' and computer == 'rock':
        print('User Won')
    elif user == 'rock' and computer == 'lizard':
        print('User Won')
    elif user == 'lizard' and computer == 'spock':
        print('User Won')
    elif user == 'spock' and computer == 'scissors':
        print('User Won')
    elif user == 'scissors' and computer == 'lizard':
        print('User Won')
    elif user == 'lizard' and computer == 'paper':
        print('User Won')
    elif user == 'paper' and computer == 'spock':
        print('User Won')
    elif user == 'spock' and computer == 'rock':
        print('User Won')
    else:
        print(computer)
        print(user)
        print("Computer Won")