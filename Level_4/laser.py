import math

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

def compare(dim, shooter, target, distance):
	tlist = reflectedTargets(dim, shooter, target, distance)
	print tlist
	slist = reflectedShooter(dim, shooter, distance)

def inRange(shooter,target,distance):
	d = (shooter[0] - target[0])**2 + (shooter[1] - target[1])**2
	if d <= distance**2:
		return math.sqrt(d)
	else:
		return False

compare([4,4], [1,1], [2,2], 100)
# print reflected( 5, 2 , 1, 12)


