from random import randint
# import matplotlib.pyplot as plt


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
	return (1,b)

def verify():
	sx = []
	sy = []
	t = open('trues', 'w')
	f = open('falses', 'w')
	n = False
	# for gg in range(0,2000):
	# 	k = createrandpair()
	# 	# print(k)
	# 	a = test(2,gg)
	# 	# b = test2(k[0],k[1])

	# 	# if not (a[0] == b):
	# 	# 	print(a[1])
	# 	# 	print('dif')
	# 	# else:
	# 	# 	print('good')

	# 	if(a[0]):
	# 		n = True;
	# 		s = a[1]
	# 		sx.append(s[0])
	# 		sy.append(s[1])
	# 		print(a[1])
	# 		t.write(str(a[1])+"\n")
		# else:
			# f.write(str(a[1])+"\n")
	# print(n)
	# for gg in range(0,2000):
		# k = createrandpair()
		# # print(k)
		# a = test(1,gg)
		# b = test2(k[0],k[1])

		# if not (a[0] == b):
		# 	print(a[1])
		# 	print('dif')
		# else:
		# 	print('good')

		# if(a[0]):
		# 	n = True;
		# 	s = a[1]
		# 	sx.append(s[0])
		# 	sy.append(s[1])
		# 	print(s[1])
		# 	t.write(str(a[1])+"\n")
	for gg in range(0,5000):
		k = createrandpair()
		# print(k)
		a = test(8,gg)
		# b = test2(k[0],k[1])

		# if not (a[0] == b):
		# 	print(a[1])
		# 	print('dif')
		# else:
		# 	print('good')

		if(a[0]):
			n = True;
			s = a[1]
			sx.append(s[0])
			sy.append(s[1])
			print(s[1])
			t.write(str(a[1])+"\n")

	plt.plot(sx,sy, "o")
	axes = plt.gca()
	axes.set_xlim([-1,3])
	# axes.set_ylim([ymin,ymax])
	plt.yscale('log')
	plt.show()
	t.close()
	f.close()

verify()

k = createrandpair()

# print(test(k[0],k[1]))
# print(test2(k[0],k[1]))
print(test(3,765))
# print(test2(57,135))