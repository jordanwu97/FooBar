cnt = 0
def answer(n):
	# print(n,m)
	if n<=2:
		return n

	a = n/2+1
	b = n/2

	if(n % 2 == 0):
		b = n/2-1

	for num in range(1, b + 1):
		print (n-num,num)
		global cnt
		cnt += 1
		answer(num)

sum(k>=0, x^((k^2+k)/2) / prod(j=1..k, 1-x^j)) - 1/(1-x)
# 
answer(12)
print cnt