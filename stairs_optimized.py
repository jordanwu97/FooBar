import math as m

# http: /  / www.learningace.com / doc / 2568736 / b42b417e56ba21d3df050ae1ec4496ba / partitionsq
# Used the algorithm described in this

csum = 0

sample = [1, 1, 1, 2, 2, 3, 4, 5]


def q(n):

	if(n < len(sample)):

		# print(n,sample[n])
		return sample[n]

	top = int(m.sqrt(n))

	s = 0

	for k in range(1, top + 1):
		# print(str(n) + ' - ' + str(k ** 2))

		# print(2 * ((-1) ** (k + 1)) * q(n-k ** 2))

		s = s + (2 * ((-1) ** (k + 1)) * q(n - k ** 2))

	return s + sigma(n)


def answer(n):

	if(n < len(sample)):
		return (sample[n])-1

	for x in range(len(sample), n + 1):
		l = q(x)
		sig = sigma(x)
		# print('appended',l + sig,'to',x)
		sample.append(l)
	return sample[len(sample)-1]-1


def sigma(n):

	for j in range(1, n):
		if j * (3 * j + 1) / 2 == n or j * (3 * j - 1) / 2 == n:
			return (-1) ** j
	return 0


print(answer(30))


# for x in range (0, len(verify)):
#   if(verify[x] == answer(x)):
#       print True
#   else:
#       print False
