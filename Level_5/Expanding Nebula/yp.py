import itertools

ones = set()

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
        
        for grid in curgrids: # for each grid in gridset, we'll try to expand it
            new_curgrids = [] # empty set for the new curgrids
            
            for comb in combs: # for each possible combinations of the next row
                ng = (grid[n], comb) # create a 2x2 grid from the previous row with the new combinations
                
                if minimize(ng) == g[n][0]:
                    g2 = [] # whatever ng that matches with what we need
                    
                    for pgr in grid: # we'll create a new grid that extends to current g[n]
                        g2.append(pgr)
                    g2.append(comb) # add in the last row
                    new_curgrids.append(tuple(ng)) 

        curgrids = tuple(new_curgrids) # curgrids will be the new set of grids that fit up to n

    pass

def expand_x(grids):
    pass

def initialize(g):
    g00 = g[0][0]
    l = set()
    dim_1 = itertools.product(range(2), repeat = 2) # use itertools to create matrix
    grids = tuple(itertools.product(dim_1, repeat = 2)) # matrices are just products of products of a a list of prossible numbers
    for grid in grids:
        if minimize(grid) == g00:
            l.add(grid)
    return tuple(l)

def answer(g):
    grids = initialize(g)