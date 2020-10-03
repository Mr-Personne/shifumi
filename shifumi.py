import random

print('shifumi start')

hands = ['rock', 'paper', 'scissors']
#print(hands[2])

playagain = 'y'

while playagain == 'y':
    # generate random computer hand
    randIndex = random.randint(0, 2)
    randHand = hands[randIndex]
    # print('randgen = ', randHand)


    # ask for player hand input and check if it's a correct hand to use
    playerHand = input('What hand will you play? ==> ')
    while playerHand not in hands:
        playerHand = input('Unknown hand, please choose between "rock", "paper" or "scissors" ==> ')
        # print('playerHand = ', playerHand)
    else:
        pass


    print('player hand : ', playerHand, ' vs computer ', randHand)
    # compare hands and declare winner
    if playerHand == 'rock' and randHand == 'paper':
        print('Computer wins with paper over rock')
        playagain = input('Playagain? y/n ==> ')

    elif playerHand == 'rock' and randHand == 'scissors':
        print('Player wins with rock against scissors')
        playagain = input('Playagain? y/n ==> ')

    elif playerHand == 'paper' and randHand == 'scissors':
        print('Computer wins with scissors against paper')
        playagain = input('Playagain? y/n ==> ')

    elif playerHand == 'paper' and randHand == 'rock':
        print('Player wins with paper against rock')
        playagain = input('Playagain? y/n ==> ')

    elif playerHand == 'scissors' and randHand == 'rock':
        print('Computer wins with rock against scissors')
        playagain = input('Playagain? y/n ==> ')

    elif playerHand == 'scissors' and randHand == 'paper':
        print('Player wins with scissors against paper')
        playagain = input('Playagain? y/n ==> ')

    else:
        print('Same hands, choose again...')
        playagain = 'y'

    
else:
    print('goodbye')