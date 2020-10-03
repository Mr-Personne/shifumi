import random

print('shifumi start')

hands = ['rock', 'paper', 'scissors']
playerScore = 0
computerScore = 0
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
        print('Computer wins with paper over rock :,(')
        computerScore = computerScore + 1
        playagain = input('Playagain? y/n (Default yes) ==> ') or 'y'

    elif playerHand == 'rock' and randHand == 'scissors':
        print('Player wins with rock against scissors :D')
        playerScore = playerScore + 1
        playagain = input('Playagain? y/n (Default yes) ==> ') or 'y'

    elif playerHand == 'paper' and randHand == 'scissors':
        print('Computer wins with scissors against paper :,(')
        computerScore = computerScore + 1
        playagain = input('Playagain? y/n (Default yes) ==> ') or 'y'

    elif playerHand == 'paper' and randHand == 'rock':
        print('Player wins with paper against rock :D')
        playerScore = playerScore + 1
        playagain = input('Playagain? y/n (Default yes) ==> ') or 'y'

    elif playerHand == 'scissors' and randHand == 'rock':
        print('Computer wins with rock against scissors :,(')
        computerScore = computerScore + 1
        playagain = input('Playagain? y/n (Default yes) ==> ') or 'y'

    elif playerHand == 'scissors' and randHand == 'paper':
        print('Player wins with scissors against paper :D')
        playerScore = playerScore + 1
        playagain = input('Playagain? y/n (Default yes) ==> ') or 'y'

    else:
        print('Same hands, choose again...')
        playagain = 'y'


    #score display...and comments...
    print('Player Score = ', playerScore, " / Computer Score = ", computerScore)
    computerWinRate = computerScore - playerScore

    if computerWinRate == 5:
        print("-- it's okay, it happens, I'm just lucky I guess --")
    elif computerWinRate == 10:
        print('-- um, waw, look at that... guess I must be really lucky today huh... --')
    elif computerWinRate == 15:
        print("-- ...I swear I'm not cheating ^^' ... --")
    elif computerWinRate > 15:
        print('-- ... --')

    
else:
    print('goodbye')