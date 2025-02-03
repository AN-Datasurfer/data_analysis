import numpy as np
np.random.seed()
outcomes = []
for x in range(100) :
    coin = np.random.randint(0, 2) #.randint() random integer
    if coin == 0 :
      outcomes.append("heads") #.append() adds element to the list
    else :
      outcomes.append("tails")

print(outcomes)


