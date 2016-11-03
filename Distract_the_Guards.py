from random import randint
from fractions import Fraction as fr
# import matplotlib.pyplot as plt

s = set()
y=1

for x in xrange(30):
	y = y * 2
	s.add(y)

def test1(a,b):
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

def check_if_int_div(a,b):
	if (float(a)/float(b)).is_integer():
		return int(float(a)/float(b))
	else:
		return False

def test2(a,b):
	c = min(a,b)
	t = a + b

	frac_t = fr(t,c).numerator

	if t in s or frac_t in s:
		return True
	else:
		return False


def createrandpair():
	a = randint(1,2000)
	b = randint(1,2000)
	return a,b

def generateList():
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

def verification():
	for i in range(0,100000):
		r = createrandpair()
		a = test1(r[0],r[1])
		b = test2(r[0],r[1])
		if not a[0] == b:
			print r
			print 'failed'
	print 'all cases pass'

verification()

# r = createrandpair()
# print(r)
# print(test2(r[0],r[1]))

# print(test1(480,4640)[0])

# print(checkintdiv(9+5,5))

# print(fr(3040,855).numerator)
