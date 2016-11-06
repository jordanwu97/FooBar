from random import randint
from fractions import Fraction as fr
# import matplotlib.pyplot as plt

s = set([4096, 1024, 2, 4, 8192, 4294967296L, 
		8, 128, 134217728, 256, 16, 8388608, 512, 
		17179869184L, 4194304, 16777216, 524288, 
		32, 131072, 262144, 33554432, 16384, 
		34359738368L, 1048576, 32768, 64, 
		2147483648L, 2048, 268435456, 8589934592L, 
		67108864, 536870912, 2097152, 65536, 1073741824]) #Set of 2^k where 0<k<31
# y=1

# for x in xrange(35):
# 	y = y * 2
# 	s.add(y)

def test1(num):
#Original iterative algorithm. Does not actually achieve O(n). 
#High memory usage and time complexity when given pairs with long loops
	a = num[0]
	b = num[1]
	t = num[1] + num[0]
	l = set()
	count = 0

	while True:

		count += 1

		if a in l or b in l:
			return False , (a,b)

		if a == b:
			c = min(num[0],num[1])
			frac_t = fr(t,c)

			return True, frac_t

		if a > b:
			l.add(a)
			a -= b
			b += b

		elif b > a:
			l.add(a)
			b -= a
			a += a


def test2(num):
#O(1) algorithm. Created using OEIS, and logrithmic graphing
	c = min(num[0],num[1])
	t = num[0]+num[1]

	frac_t = fr(t,c).numerator

	if t in s or frac_t in s:
		return True
	else:
		return False


def createrandpair(x):
#Creates random tuple pair a,b for testing
	a = randint(1000,x)
	b = randint(1000,x)
	return a,b


def generateList():
#Generates a list from O(n) algorithm for testing against faster O(1) algorithm
	t = open('trues', 'w')
	f = open('false_pos', 'w')

	for i in range(2000,4000):
		for j in range(2000,4000):
			a = test1((i,j))

			if a[0] == True :
				# print a
				f.write(str(a[1])+"\n")

	t.close()
	f.close()

generateList()


def verification():
#Verification loop over x amount of random points
	a = True
	b = True
	count = 0
	false_pos = []
	for i in xrange(2**18,2**18+1000):
		for j in xrange(2**18,2**18+1000):
			r = (i,j)
			b = test2(r)
			if b == True:
				a = test1(r)[0]
				if a != b:
					count += 1
					false_pos.append(r)

	print false_pos


# verification()

def createEdges(l):
#Creates graph G such that iter(G) contains vertices, G[v] contains vertices adjacent to v
	graph = {} #empty graph

	f = open('test', 'w')
	for x in xrange(len(l)):
		adjacent_vertices = set() #empty set
		for y in xrange(0,len(l)):
			if not test2(l[x] , l[y]):
				adjacent_vertices.add(l[y]) #add neighbor to set if fails test

		graph[l[x]] = adjacent_vertices #set of neighbors as dict[v]

	return graph

def findTerminatingPair():
	k = createrandpair(2**30)

	while test1(k) is False:
		k = createrandpair(2**30)

	print (k)
	return (k)

# print(test1((2385, 6257)))
# print(test2((2385, 6257)))