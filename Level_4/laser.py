import math
from decimal import Decimal

def reflected(dim, shooter, target, distance):

	delta_l = (dim-target)*2 	# longer reflection length
	delta_s = (target)*2 		# shorter relfection length

	farthest_pos = shooter+distance 	# farthest the shooter can shoot
	farthest_neg = shooter-distance

	temp = target
	cnt = 0
	l = []

	while temp <= farthest_pos:			# reflect targets continuously until we get to farthest_pos
		l.append(temp)
		if cnt % 2 == 0:
			temp += delta_l
		else:
			temp += delta_s
		cnt += 1


	temp = target - delta_s
	l2 = []

	while temp > farthest_neg:			# reflect targets continuously until we get to farthest_neg
		l2.append(temp)
		if cnt % 2 == 0:
			temp -= delta_s
		else:
			temp -= delta_l
		cnt += 1

	return l,l2

def reflectedTargets(dim, shooter, target, distance):
	dim_x, dim_y = dim
	shooter_x, shooter_y = shooter
	target_x, target_y = target

	xlist1, xlist2 = reflected(dim_x, shooter_x, target_x, distance)
	xlists = xlist1 + xlist2
	# print xlists
	ylists = reflected(dim_y, shooter_y, target_y, distance)
	# print ylists

	plist = [] # store reflected points in plist
	for x in xlists:
		for ylist in ylists:
			for y in ylist:
				iR = inRange(shooter, (x,y), distance)
				if not iR: 
				# if out of range, we will stop checking for this list of y's, since distance will only increase
					break
				else:
					plist.append((x,y,iR))
	return plist

def reflectedShooter(dim, shooter, distance):
	slist = reflectedTargets(dim, shooter, shooter, distance)
	return slist

def answer(dim, shooter, target, distance):
	tlist = reflectedTargets(dim, shooter, target, distance)
	target_map = unitVectorize(tlist,shooter)
	# print target_map

	slist = reflectedShooter(dim, shooter, distance)
	shooter_map = unitVectorize(slist,shooter)
	# print shooter_map

	target_map_filtered = {}

	for t in target_map:
		if t in shooter_map: # if such vector is in shooter_map
			if shooter_map[t] > target_map[t]: # if the distance in shooter map is greater than in target
				target_map_filtered[t] = target_map[t] # means we will hit target before we hit shooter
			else:
				pass
		else:
			target_map_filtered[t] = target_map[t]
	# print ""
	# print target_map_filtered

	return len(target_map_filtered)

def inRange(shooter,target,distance):
	d = (shooter[0] - target[0])**2 + (shooter[1] - target[1])**2
	if d <= distance**2:
		return math.sqrt(d)
	else:
		return False

# unit vectorize each point:
# store in map the vector with the shortest distance
def unitVectorize(l,shooter):
	nlist = [] # 
	vector_map = {} # map the unit vector with the vector of shortest distance
 	for n in l:
 		ux = rounding((n[0]-shooter[0])/n[2])
 		uy = rounding((n[1]-shooter[1])/n[2])
		nlist.append((ux,uy,n[2])) # tuple of (x/d, y/d, d)
	
	# print l
	# print nlist

	for m in nlist:
		v = m[0], m[1]
		if v not in vector_map:
			vector_map[v] = m[2]
		else:
			if vector_map[v] > m[2]: # if the distance stored in vector map is greater than the current vector we are comparing
				vector_map[v] = m[2]
			else:
				pass

	# print vector_map
	return vector_map

def rounding(x):
	return round(Decimal(x),14)

print answer([3,3], [1,1], [2,2], 5)
# print reflected( 5, 2 , 1, 12)


