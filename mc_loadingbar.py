import os
from time import sleep


def loadots():
    start = ''
    graphic = '.'
    iter = 0
    while iter < 10:
        i = 0
        holder = start
        if holder == start:
            while i in range(3):
                holder = holder + " " + graphic
                print("Your program is loading" + holder)
                sleep(0.5)
                os.system('clear')
                i += 1
        iter += 1
        # Number of iterations for testing purposes:
        #print(str(iter), "iter")


print("Program started")
loadots()
print("Program ended")
