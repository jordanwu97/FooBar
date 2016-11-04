from random import randint
from fractions import Fraction as fr
# import matplotlib.pyplot as plt

s = set() #Set of 2^k where 0<k<31
y=1

for x in xrange(30):
	y = y * 2
	s.add(y)

def test1(a,b):
#Original iterative algorithm. Does not actually achieve O(n). 
#High memory usage and time complexity when given pairs with long loops
	k = (a,b)
	l = set()

	while True:

		# print(a,b)

		if (b,a) in l or (a,b) in l:
			# print('did not exit')

			nl = []
			nl2 = []
			# print (l)
			u = len(l)
			
			for y in l:
				nl.append(y[0])
				nl2.append(y[1])

			# print (nl)
			# plt.plot(range(0,u),nl)
			# plt.plot(range(0,u),nl2)
			# plt.show()

			return (False,k)

		if a == b:
			# print('exit')
			nl = []
			nl2 = []
			# print (l)
			u = len(l)
			
			for y in l:
				nl.append(y[0])
				nl2.append(y[1])

			# print (nl)
			# plt.plot(range(0,u),nl)
			# plt.plot(range(0,u),nl2)
			# plt.show()

			return (True,k,(a,b))

		if a > b:
			l.add((a,b))
			prev = a
			a -= b
			b += b
		elif b > a:
			l.add((a,b))
			prev = b
			b -= a
			a += a


def test2(a,b):
#O(1) algorithm. Created using OEIS, and logrithmic graphing
	c = min(a,b)
	t = a + b

	frac_t = fr(t,c).numerator

	if t in s or frac_t in s:
		return True
	else:
		return False


def createrandpair(x):
#Creates random tuple pair a,b for testing
	a = randint(1,x)
	b = randint(1,x)
	return a,b


def generateList():
#Generates a list from O(n) algorithm for testing against faster O(1) algorithm
	sx = []
	sy = []
	t = open('trues', 'w')
	f = open('falses', 'w')
	n = False

	for i in range(0,10):
		for j in range(0,2000):
			k = createrandpair()
			a = test(i,j)

			if(a[0]):
				n = True;
				s = a[1]
				sx.append(s[0])
				sy.append(s[1])
				print(s[1])
				t.write(str(a[1])+"\n")
			else:
				f.write(str(a[1])+"\n")
	t.close()
	f.close()


def verification(x, randrange):
#Verification loop over x amount of random points
	for i in range(0,x):
		r = createrandpair(randrange)
		a = test1(r[0],r[1])
		b = test2(r[0],r[1])
		if not a[0] == b:
			print r
			print 'failed'
	print 'all cases pass'
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

# verification()
print(createEdges([1, 7, 3, 21, 13, 19]))
