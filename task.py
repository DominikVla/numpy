import numpy as np
from numpy import random
max = int(input ("How many dice roles would you like? "))
numbers = []
numbers = np.random.randint(1, 6, max)
print (numbers)
add = 0
count = 0
for i in range (max):
    add = add + numbers[count]
    count = count + 1
avg = add / max
print ("Average: ", avg)
