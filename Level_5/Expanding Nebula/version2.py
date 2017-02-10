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

column_combination = {}

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

def expandY(matchColumn): # expanding horizontally

    def initialize(g):
        g0 = g[0]
        l = []
        for grid, value in minimize.iteritems():
            if value == g0:
                l.append(grid)
        return tuple(l)

    combs_y = ((0,0),(0,1),(1,0),(1,1))
    curgrids = initialize(matchColumn) # initial grid set

    for n in xrange(1,len(matchColumn)): # loop until we get desired possibilites for this column

        new_curgrids = [] # empty set for the new curgrids
        for grid in curgrids: # for each grid in gridset, we'll try to expand it

            for comb in combs_y: # for each possible combinations of the next row

                ng = (grid[n], comb) # create a 2x2 grid from the previous row with the new combinations
                
                if minimize[ng] == matchColumn[n]:
                    g2 = list(grid) # whatever ng that matches with what we need
                    g2.append(comb) # add in the last row
                    new_curgrids.append(tuple(g2)) # perform colrowswap here instead

        curgrids = tuple(new_curgrids) # curgrids will be the new set of grids that fit up to n
    
    return doForAll(curgrids, colRowSwap)

def expandY2(prevColumns, matchColumn): # this will expand columns from 2 on.
    # Will only create new combinations based on previous columns to improve efficieny
    combs_initial = ((0,0),(0,1),(1,0),(1,1))
    results = []

    for pC in prevColumns:
        cc = []

        for ini in combs_initial: # initialize each row with a 2x1 that fits matchColumn
            if minimize[((pC[0], pC[1]), ini)] == matchColumn[0]:
                cc.append(ini)

        for y in xrange(1, len(matchColumn)): # go the full height of the grid
            new_cc = []

            if len(cc) == 0: # if we didn't have any grids to make from, break out of loop
                break
            
            for column in cc: # for every single (part) of the next column
                for bit in xrange(2):
                    temp_col = list(column) # make copy of column
                    if minimize[((pC[y], pC[y+1]), (column[y], bit))] == matchColumn[y]:
                        temp_col.append(bit)
                        new_cc.append(temp_col) # available as new column combination

            cc = new_cc # replace cc with new_cc to continue list

        [results.append((pC, tuple(c))) for c in cc] # for all in cc, we'll add to results

    return tuple(results)


def expandX(match_g):
    # for this part will construct a dictionary of the number of combinations at each layer. We can ignore all previous layer information
    # since they don't matter and won't be compared with anymore
    # swap columns and rows for convinence in constructing level grids later
    rotated_match_g = colRowSwap(match_g)
    
    d1 = {} # d1 will store previous row information, Key will be the row, value will be the number of grids that have the previous row
    grids = getColumnCombinations(rotated_match_g[0]) # once we get the possible columns back, we'll rotate it so its easier to match it row by row
    # grids = expandY(rotated_match_g[0])

    for grid in grids: # create initial d1
        if grid[1] not in d1:
            d1[grid[1]] = 1
        else:
            d1[grid[1]] = d1[grid[1]] + 1

    for n in xrange(1,len(rotated_match_g)):
        d2 = {} # d2 will store new layer information. will replace d1
        grids = expandY2(d1 ,rotated_match_g[n])
        # grids = expandY(rotated_match_g[n])

        totalcount = len(grids)

        for grid in grids: # for all of the grids we got back that results in the specified column in rotated_match_g[n]
            validcount = 0
            if grid[0] in d1: # if the previous column was possible
                validcount += 1
                if grid[1] in d2: # occurence of previous rows will be *multiplied into the occurence of the current row
                    d2[grid[1]] = d1[grid[0]] + d2[grid[1]] 
                else:
                    d2[grid[1]] = d1[grid[0]]
        # print d2
        # print totalcount - validcount
        d1 = d2 # after each layer, replace d1 with d2, all previous combinations will be intrinsic to d2
    
    res = 0
    for row, count in d1.iteritems():
        res = res + count

    return res

def getColumnCombinations(match_column):
    if match_column in column_combination:
        return column_combination[match_column]

    else:
        grids = expandY(match_column)
        column_combination[match_column] = grids
        return grids

def colRowSwap(grid):
    return tuple(zip(*grid))

def doForAll(items, function):
    return tuple([function(x) for x in items])

def answer(g):
	n = expandX(g)
	return n

if __name__ == "__main__":
    g = [[True, False, True, False, False, True, True, True], [True, False, True, False, False, False, True, False], [True, True, True, False, False, False, True, False], [True, False, True, False, False, False, True, False], [True, False, True, False, False, True, True, True]]
    t1 = time()
    print answer(g)
    print time() - t1
