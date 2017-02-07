def answer(start, end):
	x,y = start
	u,v = end
	deltax = u-x
	deltay = v-y
	print deltax
	print deltay
	d = deltax + deltay 
	if d == 0:
		return 0

	if not d%2 == 0:
		return None

	if not abs(deltax) == abs(deltay):
		return 2
	else:
		return 1

print answer([0,0],[7,7])