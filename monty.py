import random

def trx(choice, monty_stall=[1,0,0]):
    monty_stall=[1,0,0]
    choice=choice
    del monty_stall[choice]
    if 1 in monty_stall:
        return 1
    else:
        return 0

def monty_hall(my_stall,N):
    wins = 0
    for i in range(N):
        choice = random.randint(0,2)
        realc = trx(choice)
        wins = wins + realc

    p = (wins/float(N))

    print("prob of winning in", N ,"simulations is", p)

my_stall = [0,0,1]
N = 100000    
monty_hall(my_stall,N)
