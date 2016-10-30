def answer(n,cnt):
	# print(n,m)
	if n<=2:
		return n

	a = n/2+1
	b = n/2
	if(n % 2 == 0):
		b = n/2-1
	cnt = cnt + (b-1)

	print cnt

	for num in range(1,b):
		print (a,num)
		answer(num,cnt)
# 
answer(15,0)