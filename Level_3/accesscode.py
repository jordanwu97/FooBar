def isMultiple(a,b):
	if b % a == 0:
		return True
	else:
		return False

def answer3(l):
	cnt = 0
	for i in range(0, len(l)-2):

		for j in range (i+1, len(l)-1):

			if (isMultiple( l[i], l[j] )):

				for k in range(j+1, len(l)):

					if(isMultiple( l[j], l[k] )):
						# print(l[i], l[j], l[k])
						cnt += 1

	return cnt

def answer2(l):
	cnt = 0
	for i in range(0, len(l)-2):
		for j in range (i+1, len(l)-1):

				for k in range(j+1, len(l)):

						print(l[i], l[j], l[k])
						cnt += 1

	return cnt

def answer(l):
	cnt = 0
	for j in range(1, len(l)-1):
		a = 0
		b = 0
		for i in range(0,j):
			if (isMultiple( l[i], l[j] )):
				print('a',l[i], l[j])
				a += 1
		for k in range(j+1,len(l)):
			if (isMultiple( l[j], l[k] )):
				print('b',l[j], l[k])
				b += 1
		cnt = cnt + a*b
	return cnt

l = list(range(1,2000))
# l.pop(0)
m = (1,1,1)

print(answer(l))

test(l)

# print(answer2(l))