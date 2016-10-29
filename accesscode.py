def isMultiple(a,b):
	if b % a == 0:
		return True
	else:
		return False

def answer(l):
	cnt = 0
	for i in range(0, len(l)-2):
		for j in range (i+1, len(l)-1):
			if (isMultiple( l[i], l[j] )):
				for k in range(j+1, len(l)):
					if(isMultiple( l[j], l[k] )):
						# print(l[i], l[j], l[k])
						cnt += 1

	return cnt

l = list(range(1,7))
# l.pop(0)
m = (2,3,5)

print(answer(l))