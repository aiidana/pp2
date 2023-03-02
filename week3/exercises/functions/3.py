
numheads=int(input())
numlegs=int(input())

def solve(numheads, numlegs):
    for i in range(1,numheads+1):
        j=numheads-i
        if 2*j+4*i ==numlegs:
            return i,j

print(solve(numheads,numlegs))
