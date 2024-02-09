"""
Write a program to solve a classic puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm. 
How many rabbits and how many chickens do we have? 
create function: solve(numheads, numlegs):

x + y = 35 => x = 35- y => 2x + 2y = 70
2y = 70 - 2x 
4x + 2y = 94 => 
4x + 70 - 2x = 94
2x = 94 -70


"""
numheads = int(input())
numlegs = int(input())
def solve(numheads, numlegs):
    chicken = 0
    rabbit = 0
    rabbit = (numlegs - 2*numheads)/2
    chicken = numheads - rabbit 
    return int(chicken), int(rabbit)

print(solve(numheads, numlegs))