import itertools

def createGrids(w,h):
	dim_1 = itertools.product(range(2), repeat = w) # use itertools to create matrix
	return tuple(itertools.product(dim_1, repeat = h)) # matrices are just products of products of a a list of prossible numbers

def pruneGrids(grids):
	l = len(grids[0]) # grab the height of 1 grid
	row_combinations = list(itertools.permutations(range(l),l)) 

	map = set()
	for grid in list(grids): # for each specific grid
		gridexist = False
		for rc in row_combinations: # for each different row combination
			ng = []
			i = 0
			for row in grid: # for each row in each specific grid
				# print grid[rc[i]]
				ng.append(grid[rc[i]]) # assign ng rows based on row combination
				i += 1

			ng = tuple(ng)
			if ng in map: # if this combination of grid already exist in map
				gridexist = True
				break

		if gridexist == False:
			map.add(ng)

	return map

def printResult(n):
	for i in n:
		for j in i:
			print j
		print ""

if __name__ == "__main__":
	mygrids = createGrids(2,3)
	mygrids = pruneGrids(mygrids)
	printResult(mygrids)