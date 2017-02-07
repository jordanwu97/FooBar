import itertools
from time import time

def createGrids(w,h,d):
	dim_1 = itertools.product(range(d), repeat = w) # use itertools to create matrix
	return tuple(itertools.product(dim_1, repeat = h)) # matrices are just products of products of a a list of prossible numbers

def printgrid(n):
	for i in n:
		print i
	print ""

def pruneGrids(grids, match):
    h = len(grids[0]) - 1
    w = len(grids[0][0]) - 1

    def minimize(y,x):
        if (grid[y][x] + grid[y+1][x] + grid[y][x+1] + grid[y+1][x+1]) == 1:
            return 1
        else:
            return 0
    
    count = 0

    for grid in grids:
        ng = [[0 for x in range(w)] for y in range(h)]

        for y in xrange(h):
            for x in xrange(w):
                ng[y][x] = minimize(y,x)

        ng = tuple(tuple(x)for x in ng)
        # print ng
        if ng == match:
            count += 1
            # printgrid(grid)

    return count

def answer(c):
    t1 = time()
    g1s = createGrids(len(c[0])+1,len(c)+1,2)
    # print g1s
    lol = pruneGrids(g1s, c)
    t2 = time()
    print t2-t1
    print lol

answer(c)