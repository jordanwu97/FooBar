cnt = 0

def answer(n,check):
	if n<=2:
		# print('bottom')
		return n
	halfn_minus_1 = (((n-1)/2)-1)
	# print(halfn_minus_1)

	for i in range(n-1,0,-1):
		b = n - i
		# print(check,i,b)  
		# print(i)
		# print(check)

		if (i>=check):
			print('check',check,i)
			# print('wtf')
			# print(i,b,'ng')
			break

		if (i>b):
			if(check==200):
				print(i)
				print (check,i,b, 'g')
			global cnt 
			cnt += 1

		# answer(b,i)

answer(200,200)

# print(sum(range(0,6)))

print cnt