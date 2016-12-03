import math
from decimal import Decimal

def reflected(dim, shooter, target, distance):

	delta_l = (dim-target)*2 	# longer reflection length
	delta_s = (target)*2 		# shorter relfection length

	farthest_pos = shooter+distance 	# farthest the shooter can shoot
	farthest_neg = shooter-distance

	temp = target
	cnt = 0
	l = []								# list of positive points

	while temp <= farthest_pos:			# reflect targets continuously until we get to farthest_pos
		l.append(temp)
		if cnt % 2 == 0:
			temp += delta_l
		else:
			temp += delta_s
		cnt += 1


	temp = target - delta_s
	l2 = []								# list of negative points

	while temp >= farthest_neg:			# reflect targets continuously until we get to farthest_neg
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
					x = (x - shooter[0]) # (vector x,y,distance from shooter)
					y = (y - shooter[1])
					ux = round((x/iR), 15)
					uy = round((y/iR), 15)
					plist.append((ux, uy, x, y, iR))
	return plist

def reflectedShooter(dim, shooter, distance):
	slist = reflectedTargets(dim, shooter, shooter, distance)
	return slist

def inRange(shooter, target, distance):
	d = (shooter[0] - target[0])**2 + (shooter[1] - target[1])**2
	if d <= distance**2:
		return math.sqrt(d)
	else:
		return False

# find the shortest distance corresponding with each vector P[v], where v:Distance
# store in map the vector with the shortest distance
def findShortest(l,shooter):
	vector_map = {} # map the unit vector with the vector of shortest distance
	c = 0

	for m in l:
		v = m[0], m[1], c

		if v not in vector_map:
			vector_map[v] = m[2],m[3],m[4]
		else:
			selected_vector = vector_map[v]
			if ((selected_vector[0], selected_vector[1]), v): 
				if vector_map[v] > m[2]: # if the distance stored in vector map is greater than the current vector we are comparing
					vector_map[v] = m[2],m[3],m[4]
			else:
				c += 1
				v = m[0], m[1], c

	return vector_map

def isSameDirection(u, v):
	sign = lambda a: (a>0) - (a<0)

	ux, uy = u
	vx, vy = v

	z = ux*vy - uy*vx
	if z == 0:
		if sign(ux) == sign(vx) and sign(uy) == sign(vy):
			return True
		else:
			return False
	else:
		return False

def answer(dim, shooter, target, distance):
	tlist = reflectedTargets(dim, shooter, target, distance)
	# print tlist
	target_map = findShortest(tlist,shooter)
	# print target_map

	slist = reflectedShooter(dim, shooter, distance)
	# print slist
	shooter_map = findShortest(slist,shooter)
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

def rounding(x):
	return round(Decimal(x),13)

print answer([300, 275], [150, 150], [185, 100], 500)