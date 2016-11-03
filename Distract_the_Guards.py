from random import randint
import matplotlib.pyplot as plt


def test(a,b):
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
			plt.plot(range(0,u),nl)
			plt.plot(range(0,u),nl2)
			plt.show()

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
			plt.plot(range(0,u),nl)
			plt.plot(range(0,u),nl2)
			plt.show()

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
	k = (a,b)
	t = a + b
	if not t % 2 == 0:
		return False

	else:
		return True
	# t2 = t/2
	# while True:
	# 	if a < b:
	# 		if a > t2:
	# 			return False
	# 		elif a == t2:
	# 			return True
	# 		a = a*2

	# 	if b < a:
	# 		if b > t2:
	# 			return False
	# 		elif a == t2:
	# 			return True
	# 		b = b*2


def createrandpair():
	a = randint(0,454)
	b = randint(0,454)
	return (a,b)

def verify():
	t = open('trues', 'w')
	f = open('falses', 'w')
	n = False
	for _ in range(0,100):
		k = createrandpair()
		# print(k)
		a = test(k[0],k[1])
		b = test2(k[0],k[1])

		if not (a[0] == b):
			print(a[1])
			print('dif')
		# else:
		# 	print('good')

		# if(a[0]):
		# 	n = True;
		# 	print(a[1])
		# 	t.write(str(a[1])+"\n")
		# else:
		# 	f.write(str(a[1])+"\n")
	# print(n)
	t.close()
	f.close()

# verify()

k = createrandpair()

# print(test(k[0],k[1]))
# print(test2(k[0],k[1]))
print(test(57,135))
# print(test2(57,135))