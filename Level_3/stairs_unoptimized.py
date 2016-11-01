import math as m

sample = [	1, 1, 1, 2, 2, 3, 4, 5, 6, 8,
		   10, 12, 15, 18, 22, 27, 32, 38, 46, 54]


def sigma(n):
	for j in range(1, n):
		if j * (3 * j + 1) / 2 == n or j * (3 * j - 1) / 2 == n:
			return (-1)**j
	return 0


def q(n):

	if (n < len(sample)):

		# print(n,sample[n])
		return sample[n]

	top = int(m.sqrt(n))

	s = 0

	for k in range(1, top + 1):
		# print(str(n)+' - '+str(k**2))

		# print(2*((-1)**(k+1))*q(n-k**2))

		s = s + (2 * ((-1) ** (k + 1)) * q(n - k ** 2))

	return s + sigma(n)


print(q(50))
