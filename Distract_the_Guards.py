from random import randint

l = set()

def test(a,b):
	k = (a,b)

	while True:

		print(a,b)

		if (b,a) in l or (a,b) in l:
			# print('did not exit')
			return (False,k)

		if a == b:
			# print('exit')
			return (True,k)

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


def createrandpair():
	a = randint(0,4534)
	b = randint(0,4583)
	return (a,b)

def verify():
	t = open('trues', 'w')
	f = open('falses', 'w')
	n = False
	for _ in range(0,1000):
		k = createrandpair()
		# print(k)
		a = test(k[0],k[1])
		if(a[0]):
			n = True;
			print(a[1])
			t.write(str(a[1])+"\n")
		else:
			f.write(str(a[1])+"\n")
	print(n)
	t.close()
	f.close()

# verify()

print(test(1343,2014))