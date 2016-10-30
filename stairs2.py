cnt = 0

def answer(n,check):
	if n<=2:
		print('bottom')
		return n
	halfn_minus_1 = (((n-1)/2)-1)
	# print(halfn_minus_1)

	for i in range(n-1,halfn_minus_1-1,-1):
		b = n - i
		# print(i)
		# print(check)

		if (i>=check):
			print(check,i)
			print('wtf')
			# print(i,b,'ng')
			break

		if (i>b):
				print (check,i,b, 'g')
				global cnt 
				cnt += 1
		# else:
		# 	# print(i,b,'ng')
			
		# 	# answer(n-i)
		answer(b,i)

answer(12,12)
print cnt