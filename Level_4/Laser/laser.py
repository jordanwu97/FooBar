import math
from decimal import Decimal
# import matplotlib.pyplot as plt

# What doesn't work:
# handling conflict resolution and hash_maping unit vectors

# What to try:
# Force corners to be off limit in original cap list

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

def findVector(dim, shooter, target, distance):
	dim_x, dim_y = dim
	shooter_x, shooter_y = shooter
	target_x, target_y = target

	xlist1, xlist2 = reflected(dim_x, shooter_x, target_x, distance)
	xlists = xlist1 + xlist2
	# print xlists
	ylists = reflected(dim_y, shooter_y, target_y, distance)
	# print ylists

	# plist = [] # store reflected points in plist
	v_map = {}

	for x in xlists:
		for ylist in ylists:
			for y in ylist:
				iR = inRange(shooter, (x,y), distance)
				if not iR: 
				# if out of range, we will stop checking for this list of y's, since distance will only increase
					break
				else:
					vx = x - shooter[0]
					vy = y - shooter[1]
					ux = rounding((x - shooter[0]) / iR) # unit vector for each
					uy = rounding((y - shooter[1]) / iR)
					uv = (ux,uy)
					v = (vx,vy)
					# plist.append((ux, uy, iR, vx, vy))

					# find the shortest distance corresponding with each vector v_map[uv], where uv:Distance
					# store in map the vector with the shortest distance
					if uv not in v_map:
						v_map[uv] = iR, v
					else:
						pass
						selected = v_map[uv]
						# print selected
						# if not isSameDirection(v, selected[1]): # double checking assumption that if unit vectors are equal, then parallel
							# return (1/0) # throw a zero division error if assumption is false
						if selected[0] > iR: # if the distance stored in vector map is greater than the current vector we are comparing
							print 'conflict'
							vector_map[uv] = iR, v
						else:
							pass
	return v_map
	# return plist

def inRange(shooter, target, distance):
	d2 = (shooter[0] - target[0])**2 + (shooter[1] - target[1])**2 # pythagoras!
	if d2 <= distance**2:
		return math.sqrt(d2)
	else:
		return False

def isSameDirection(u, v):
	sign = lambda a: (a>0) - (a<0)

	ux, uy = u
	vx, vy = v

	z = ux*vy - uy*vx # solve for k component of (u x v)
	if z == 0 and (sign(ux) == sign(vx) and sign(uy) == sign(vy)): # cross must be 0 AND signs of components must be the same
		return True
	else:
		return False

def restrictedUnitVectors(v,distance):
	d = inRange((0,0),v,distance)
	uv = (v[0]/d, v[1]/d)

	return uv, d

def answer(dim, shooter, target, distance):

	# dictionary of vectors for shooter and target
	sx, sy = shooter
	dimx, dimy = dim

	target_map = findVector(dim, shooter, target, distance) 
	shooter_map = findVector(dim, shooter, shooter, distance)

	restricted_1 = dimx-sx, dimy-sy, 
	restricted_2 = -sx,-sy
	restricted_3 = dimx-sx, -sy
	restricted_4 = -sx, dimy-sy

	restricteds = [restricted_1,restricted_2,restricted_3,restricted_4]

	u_restricteds = []

	for n in restricteds:
		k = restrictedUnitVectors(n, distance)
		shooter_map[k[0]] = k[1], n

	target_map_filtered = {}

	for t in target_map:
		if t in shooter_map: # if such vector is in shooter_map
			if shooter_map[t] > target_map[t]: # if the distance in shooter map is greater than in target
				print 'shooter target conflict'
				target_map_filtered[t] = target_map[t] # means we will hit target before we hit shooter
			else:
				pass
		else:
			target_map_filtered[t] = target_map[t]
	
	# plt.scatter(shooter[0],shooter[1])

	# for key, value in target_map_filtered.iteritems():
	# 	n = value[1]
		# plt.scatter(n[0]+shooter[0],n[1]+shooter[1])

	# plt.show()
	return len(target_map_filtered)

def rounding(x):
	return round(Decimal(x),9)

print answer([300, 275], [150, 150], [185, 100], 500)