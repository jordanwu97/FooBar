import itertools

def createGrids(w,h,d):
	dim_1 = itertools.product(range(d), repeat = w) # use itertools to create matrix
	return tuple(itertools.product(dim_1, repeat = h)) # matrices are just products of products of a a list of prossible numbers

def pruneGrids(grids):
	l = len(grids[0]) # grab the height of 1 grid
	w = len(grids[0][0])
	row_combinations = list(itertools.permutations(range(l),l))
	col_combinations = list(itertools.permutations(range(w),w))

	map = set()
	for grid in list(grids): # for each specific grid

		# printgrid(grid)

		if grid in map: # if this grid already exist in the map, automatically skip the rest
			continue

		gridexist = False
		for rc in row_combinations: # for each different row combination

			ng = reorganizeRows(grid, rc) # reorganize based on row combination scheme

			if ng in map:
				break

			for cc in col_combinations: # redo row combinations but for columns
				ng2 = colRowSwap(ng) # swap columns rows
				ng2 = reorganizeRows(ng2, cc) # reorganize based on column combination scheme
				ng2 = colRowSwap(ng2) # put back

				if ng2 in map: # if this combination of grid already exist in map
					gridexist = True
					break

			if gridexist:
				break

		if not gridexist:
			map.add(ng)

	return map

def printgrid(n):
	for i in n:
		print i
	print ""

def reorganizeRows(grid, scheme):
	# print grid, scheme
	ng = []
	i = 0
	for row in grid: # for each row in each specific grid
		ng.append(grid[scheme[i]]) # assign ng rows based on row combination
		i += 1

	return tuple(ng)

def colRowSwap(grid):
	w,h = len(grid), len(grid[0])
	ng = [[0 for x in range(w)] for y in range(h)]
	for n in xrange(len(grid)):
		for m in xrange(len(grid[0])):
			ng[m][n] = grid[n][m]

	return tuple(tuple(x)for x in ng) # tuplize both dimensions

def answer(h,w,d):
	mygrids = createGrids(h,w,d)
	
	mygrids = pruneGrids(mygrids)

	# for grids in mygrids:
	# 	printgrid(grids)
	print len(mygrids)

# answer(2,3,4)
gs = createGrids(2,2,2)
for g in gs:
	printgrid(g)

# go into each combination of rows
	# for each combination of rows, also need to evaluate combination of columns
	# to reorganize columns, we convert each column to rows, reorganize using the same function,
	# recreate grid again by re-assigning row into columns
	# (1, 0, 0)
	# (1, 0, 0)
	# (0, 0, 1)
	# ->
	# (1, 1, 0)
	# (0, 0, 0)
	# (0, 0, 1)
	# -> SCRAMBLE
	# -> Check new grid against map
	# -> redo grid by changing rows back into columns