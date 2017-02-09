import itertools
from time import time

minimize = {
    ((0, 0), (0, 0)) : 0,
    ((0, 0), (0, 1)) : 1,
    ((0, 0), (1, 0)) : 1,
    ((0, 0), (1, 1)) : 0,
    ((0, 1), (0, 0)) : 1,
    ((0, 1), (0, 1)) : 0,
    ((0, 1), (1, 0)) : 0,
    ((0, 1), (1, 1)) : 0,
    ((1, 0), (0, 0)) : 1,
    ((1, 0), (0, 1)) : 0,
    ((1, 0), (1, 0)) : 0,
    ((1, 0), (1, 1)) : 0,
    ((1, 1), (0, 0)) : 0,
    ((1, 1), (0, 1)) : 0,
    ((1, 1), (1, 0)) : 0,
    ((1, 1), (1, 1)) : 0,
}

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
		print i,
        print

def getProducts(l): # get all the ways to arrange 0,1 in length l
    return tuple(itertools.product(range(2), repeat = l)) 

def initialize(g):
    g0 = g[0]
    l = []
    for grid, value in minimize.iteritems():
        if value == g0:
            l.append(grid)
    return tuple(l)

def expandY(matchColumn): # expanding horizontally
    combs_y = ((0,0),(0,0),(1,0),(1,1))
    curgrids = initialize(matchColumn) # initial grid set

    for n in xrange(1,len(matchColumn)): # loop until we get desired possibilites for this column

        new_curgrids = [] # empty set for the new curgrids
        for grid in curgrids: # for each grid in gridset, we'll try to expand it

            for comb in combs_y: # for each possible combinations of the next row
                ng = (grid[n], comb) # create a 2x2 grid from the previous row with the new combinations
                
                if minimize[ng] == matchColumn[n]:
                    g2 = list(grid) # whatever ng that matches with what we need
                    g2.append(comb) # add in the last row
                    new_curgrids.append(tuple(g2)) 

        curgrids = tuple(new_curgrids) # curgrids will be the new set of grids that fit up to n
    
    return curgrids

def expandX(match_g):
    # for this part will construct a dictionary of the number of combinations at each layer. We can ignore all previous layer information
    # since they don't matter and won't be compared with anymore
    # swap columns and rows for convinence in constructing level grids later
    rotated_match_g = colRowSwap(match_g)
    
    d1 = {} # d1 will store previous row information, Key will be the row, value will be the number of grids that have the previous row
    grids = doForAll(expandY(rotated_match_g[0]), colRowSwap) # once we get the possible columns back, we'll rotate it so its easier to match it row by row
    print grids

    for grid in grids: # create initial d1
        if grid[1] not in d1:
            d1[grid[1]] = 1
        else:
            d1[grid[1]] = d1[grid[1]] + 1
    print ""
    print d1

    for n in xrange(1,len(rotated_match_g)):
        d2 = {} # d2 will store new layer information. will replace d1
        grids = doForAll(expandY(rotated_match_g[n]), colRowSwap)

        for grid in grids: # for all of the grids we got back that results in the specified column in rotated_match_g[n]

            if grid[0] in d1: # if the previous column was possible
                if grid[1] in d2: # occurence of previous rows will be *multiplied into the occurence of the current row
                    d2[grid[1]] = d1[grid[0]] + d2[grid[1]] 
                else:
                    d2[grid[1]] = d1[grid[0]]
        # print d2    
        d1 = d2 # after each layer, replace d1 with d2, all previous combinations will be intrinsic to d2
    
    res = 0
    for row, count in d1.iteritems():
        res = res + count

    return res

def colRowSwap(grid):
    return tuple(zip(*grid))

def doForAll(items, function):
    return tuple([function(x) for x in items])

def answer(g):
    return expandX(g)

g = [[True, False, True], [False, True, False]]
g = convertToBin(g)

print answer(g)