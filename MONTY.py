from random import randrange
# to compare if switching is better or not     
def monty_hall(choice, switch, doorCount):
  
    door = [0]*doorCount
    door[randrange(doorcount)] = 1
    chosen = door[choice]
    unpicked = door
    del unpicked[choice]
    TrueDoor = 1 in unpicked
    if switch:
        return TrueDoor
    else:
        return chosen

choice=random.randint(0,2)
doorCount=3
N = 10000
print "\nMonty Hall problem simulation:"
print doorCount, "doors,", N, "iterations.\n"
 
print "No switching available for you to win", 
cases1=sum(monty_hall(choice, switch=False,doorCount=3)
          for x in range(N))
p1=cases1/float(N)
print cases1
print "out of", N, "times i.e with probablity",p1

print "\nSwitching available for you to win",
cases2=sum(monty_hall(choice, switch=True,doorCount=3)
          for x in range(N))
p2=cases2/float(N)
print cases2
print "out of", N, "times i.e with probablity",p2
