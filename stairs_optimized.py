import math as m

# http://www.learningace.com/doc/2568736/b42b417e56ba21d3df050ae1ec4496ba/partitionsq
# Used the algorithm described in this

csum = 0

sample = [1, 1, 1, 2, 2, 3, 4, 5]

def q(n,pos,level):

	if(n<len(sample)):

		return ((-1)**(pos+1))*((2**level)*sample[n])

	top = int(m.sqrt(n))

	s = 0

	for k in range(1,top+1):
		# print(str(n)+' - '+str(k**2))
		s = s + q(n-k**2,k,level+1)

	return s

def answer(n):

	if(n<len(sample)):
		return (sample[n])-1

	for x in range(len(sample),n+1):
		l = 2*q(x,0,-1)
		sig = sigma(x)
		# print('appended',l+sig,'to',x)
		sample.append(l+sig)
	return sample[len(sample)-1]-1

def sigma(n):
	for j in range(1,n):
		if j*(3*j+1)/2 == n or j*(3*j-1)/2 == n:
			return (-1)**j
	return 0

print(answer(30))

# verify = [0, 0, 0, 1, 1, 2, 3, 4, 5, 7, 9, 11, 14, 17, 21, 26, 31, 37, 45, 53, 63, 75, 88, 103, 121, 141, 164, 191, 221, 255, 295, 339, 389, 447, 511, 584, 667, 759, 863, 981, 1112, 1259, 1425, 1609, 1815, 2047, 2303, 2589, 2909, 3263, 3657, 4096, 4581, 5119, 5717, 6377]

# for x in range (0, len(verify)):
# 	if(verify[x] == answer(x)):
# 		print True
# 	else:
# 		print False


