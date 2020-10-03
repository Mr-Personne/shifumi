import random

print('shifumi start')

hands = ['rock', 'paper', 'scissors']
#print(hands[2])

playagain = 'y'

while playagain == 'y':
    randindex = random.randint(0, 2)
    print('randindex = ', randindex)
    playagain = input('Playagain? y/n ==> ')
else:
    print('goodbye')