import random

def trx(choice, monty_stall=[1,0,0]):

    x=1- monty_stall[choice]
    return x
    

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
