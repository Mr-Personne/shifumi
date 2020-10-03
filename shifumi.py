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

    playagain = input('Playagain? y/n ==> ')
else:
    print('goodbye')