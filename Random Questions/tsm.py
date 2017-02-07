from math import sqrt
import itertools as it

CostMap = {}

def distance(a,b):
	x,y = a
	u,v = b
	return sqrt((x-u)**2+(y-v)**2)


nodes = [0,1,2,3]
nodelength = [[0,1,15,6],[2,0,7,3],[9,6,0,12],[10,4,8,0]]
mapofdistances = {}

listofcombi = []

for n in xrange(1,len(nodes)):
	k = list(it.combinations(nodes[1:len(nodes)], n))
	listofcombi.append(k)

# print listofcombi

for subcomb in listofcombi:
	for sublist in subcomb:
		if len(sublist) == 1:
			val = sublist[0]
			subset = (val,0)
			parent = 0
			d = nodelength[0][val]
			mapofdistances[subset] = d, parent
		if len(sublist) < 3 and len(sublist) > 1:
			sublistperms = list(it.permutations(sublist))
			for n in sublistperms:
				l = list(n)
				l.append(0)
				s1 = l[0],l[1]
				s2 = l[1],l[2]
				d1 = nodelength[l[1]][l[0]]
				d2 = mapofdistances[s2]
				d = d1 + d2[0]
				mapofdistances[s1] = d, l[1]
	

print mapofdistances


# print list(it.permutations([1,2,3],3))