import itertools
from time import time

ones = set()

def convertToBin(g):
    ng = []
    for row in g:
        ngr = []
        for i in row:
            if i:
                ngr.append(1)
            else:
                ngr.append(0)
        ng.append(ngr)
    return tuple(tuple(x)for x in ng) # tuplize both dimensions


def printgrid(n):
	for i in n:
		print i
	print ""

def printgrids(n):
    for i in n:
        printgrid(i)

def minimize1(grid): # simplify a single 2x2 grid
    if grid not in ones and len(ones) == 4:
        return 0

    if grid in ones:
        return 1

    if (grid[0][0] + grid[0][1] + grid[1][0] + grid[1][1]) == 1:
        ones.add(grid)
        return 1

    else:
        return 0

def minimize2(grid): # simplify grid size of nx2
    sim = []
    for n in xrange(len(grid[0])-1):
        ng = ((grid[0][n], grid[0][n+1]), (grid[1][n], grid[1][n+1]))
        sim.append(minimize1(ng))
    return tuple(sim)

def getProducts(l): # get all the ways to arrange 0,1 in length l
    return tuple(itertools.product(range(2), repeat = l)) 

def expand_y(grids, g): # expanding horizontally
    combs_y = getProducts(2)
    curgrids = grids # initial grid set

    for n in xrange(1,len(g)): # loop until we get desired horizontal possibilites for first column

        new_curgrids = [] # empty set for the new curgrids
        for grid in curgrids: # for each grid in gridset, we'll try to expand it

            for comb in combs_y: # for each possible combinations of the next row
                ng = (grid[n], comb) # create a 2x2 grid from the previous row with the new combinations
                
                if minimize1(ng) == g[n][0]:
                    g2 = [] # whatever ng that matches with what we need
                    
                    for pgr in grid: # we'll create a new grid that extends to current g[n]
                        g2.append(pgr)
                    g2.append(comb) # add in the last row
                    new_curgrids.append(tuple(g2)) 

        curgrids = tuple(new_curgrids) # curgrids will be the new set of grids that fit up to n
    
    return curgrids

def expand_x(grids, match_g):
    # for this part will construct a dictionary of the number of combinations at each layer. We can ignore all previous layer information
    # since they don't matter and won't be compared with anymore
    # swap columns and rows for convinence in constructing level grids later
    g2 = []
    for a in grids:
        g2.append(colRowSwap(a))
    grids = tuple(g2)
    print grids
    match_g = colRowSwap(match_g)
    
    d1 = {} # d1 will store previous row information, Key will be the row, value will be the number of grids that have the previous row
    combs_x = getProducts(len(grids[0][0]))

    for grid in grids: # create initial d1
        if grid[1] not in d1:
            d1[grid[1]] = 1
        else:
            d1[grid[1]] = d1[grid[1]] + 1
    print d1

    for n in xrange(1,len(match_g)):
        d2 = {} # d2 will store new layer information. will replace d1
        for row, count in d1.iteritems():
            for comb in combs_x:
                # construct new grid from previous row + all combinations of what next row can be
                ng_min = minimize2((row, comb)) # minimize that
                if ng_min == match_g[n]: # if minimized grid is same as match
                    if comb in d2: # combinations of previous rows will be *multiplied, into current row counts
                        d2[comb] = d2[comb] + count
                    else:
                        d2[comb] = count
        print d2
        d1 = d2 # after each layer, replace d1 with d2, all previous combinations will be intrinsic to d2
    
    res = 0
    for row, count in d1.iteritems():
        res = res + count

    return res


def initialize(g):
    g00 = g[0][0]
    l = set()
    dim_1 = itertools.product(range(2), repeat = 2) # use itertools to create matrix
    grids = tuple(itertools.product(dim_1, repeat = 2)) # matrices are just products of products of a a list of prossible numbers
    for grid in grids:
        if minimize1(grid) == g00: # prune out initial matrices just to have those that simplifies to g00
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

    grids = initialize(g) 
    grids = expand_y(grids, g)

    res = expand_x(grids, g)
    return res
g = [[True, False, True], [False, True, False]]
g = convertToBin(g)

print answer(g)