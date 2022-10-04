from random import randint
v = 0
while True:
    player = int(input('Enter Value: '))
    computer = randint(0, 10)
    tot = player + computer
    type = ' '
    while type not in 'OE':
        type = str(input('Odd or even? [O/E] ')).strip().upper()[0]
    print(f'You played {player} and Computer played {computer}. total of {tot}!')
    if type == 'E':
        if tot % 2 == 0:
            print('You won!')
            v += 1
        else:
            print('You lose!')
            break
    elif type == 'O':
        if tot % 2 == 1:
            print('You won!')
            v += 1
        else:
            print('You lose!')
            break
        print('Lets play again ??')
print(f'Game over! You won {v} times.')        

