print('R = Rock, P = Paper, S = Scissors')


def rps(p1=input("Player 1, enter your choice (r/p/s): ").lower(),
        p2=input("Player 2, enter your choice (r/p/s): ").lower()):
    if p1 == 's' and p2 == 'p' or p1 == 'p' and p2 == 'r' or p1 == 'r' and p2 == 's':
        return 'Player 1 won!'
    if p2 == 's' and p1 == 'p' or p2 == 'p' and p1 == 'r' or p2 == 'r' and p1 == 's':
        return 'Player 2 won!'
    else:
        return 'Draw!'


print(rps())
