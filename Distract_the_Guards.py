from random import randint

def test(a,b,lev,prevk):
	
	# print(a,b,lev,prevk)

	if a == b:
		print('exit')
		return True

	if a == prevk:
		print('did not exit')
		return False
	
	elif a > b:
		prev = a
		a -= 1
		b += 1
		test(a,b,lev+1,prev)
	
	elif b > a:
		prev = b
		a += 1
		b -= 1
		test(a,b,lev+1,prev)

def createrandpair():
	a = randint(0,23453)
	b = randint(0,23123)
	return (a,a+2*b+1)

k = createrandpair()

test(k[0],k[1],0,0)

for _ in range(0,1000):
	k = createrandpair()
	print(k)
	if(test(k[0],k[1],0,0)):
		print(True)
print(False)