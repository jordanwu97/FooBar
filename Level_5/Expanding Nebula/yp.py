import itertools
from time import time

ones = set()

def printgrid(n):
	for i in n:
		print i
	print ""

def printgrids(n):
    for i in n:
        printgrid(i)

def minimize(grid):
    if grid not in ones and len(ones) == 4:
        return 0

    if grid in ones:
        return 1

    if (grid[0][0] + grid[0][1] + grid[1][0] + grid[1][1]) == 1:
        ones.add(grid)
        return 1

    else:
        return 0

def getProducts(l): # get all the ways to arrange 0,1 in length l
    return tuple(itertools.product(range(2), repeat = l)) 

def expand_y(grids, g): # expanding horizontally
    combs = getProducts(2)
    curgrids = grids # initial grid set

    for n in xrange(1,len(g)): # loop until we get desired horizontal possibilites for first column

        new_curgrids = [] # empty set for the new curgrids
        for grid in curgrids: # for each grid in gridset, we'll try to expand it

            for comb in combs: # for each possible combinations of the next row
                ng = (grid[n], comb) # create a 2x2 grid from the previous row with the new combinations
                
                if minimize(ng) == g[n][0]:
                    g2 = [] # whatever ng that matches with what we need
                    
                    for pgr in grid: # we'll create a new grid that extends to current g[n]
                        g2.append(pgr)
                    g2.append(comb) # add in the last row
                    new_curgrids.append(tuple(g2)) 

        curgrids = tuple(new_curgrids) # curgrids will be the new set of grids that fit up to n
    
    return curgrids

def expand_x(grids, g):
    # for this part will construct a dictionary of the number of combinations at each layer. We can ignore all previous layer information
    # since they don't matter and won't be compared with anymore
    d1 = {}
    for grid in grids:
        if grid[1] not in d1:
            d1[grid[1]] = 1
        else:
            d1[grid[1]] = d1[grid[1]] + 1
    print d1

def initialize(g):
    g00 = g[0][0]
    l = set()
    dim_1 = itertools.product(range(2), repeat = 2) # use itertools to create matrix
    grids = tuple(itertools.product(dim_1, repeat = 2)) # matrices are just products of products of a a list of prossible numbers
    for grid in grids:
        if minimize(grid) == g00: # prune out initial matrices just to have those that simplifies to g00
            l.add(grid)
    return tuple(l)

def colRowSwap(grid):
	w,h = len(grid), len(grid[0])
	ng = [[0 for x in range(w)] for y in range(h)]
	for n in xrange(len(grid)):
		for m in xrange(len(grid[0])):
			ng[m][n] = grid[n][m]

	return tuple(tuple(x)for x in ng) # tuplize both dimensions

def answer(g):
    t1 = time()
    grids = initialize(g) 
    grids = expand_y(grids, g)

    g2 = []
    for g in grids:
        g2.append(colRowSwap(g)) # swap columns and rows for convinence in constructing level grids later
    g2 = tuple(g2)

    expand_x(g2, g)

    t2 = time()
    # printgrids(g2)
    print len(grids)
    print t2-t1

c = ((0,),(1,),)

answer(c)