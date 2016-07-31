import math


def alexa_primes(n):
	""" Get primes under n"""
	A = {i: True for i in range(2, n + 1)}
	for i in range(2, math.ceil(math.sqrt(n))):
		if A[i] is True:
			for j in [i * i + x * i for x in range(0, n + 1)]:
				A[j] = False

	# We can use a lambda, or comprehension
	# return list(filter(lambda x: A[x] is True, A.keys()))
	return [x for x in A.keys() if A[x] is True]


def gen_primes():
	"""Other sieve implementation in generator form!"""
	D = {}
	q = 2

	while True:
		if q not in D:
			yield q
			D[q * q] = [q]
		else:
			for p in D[q]:
				D.setdefault(p + q, []).append(p)
			del D[q]

		q += 1


print(alexa_primes(10))
assert alexa_primes(10) == [2, 3, 5, 7]

primes_generator = gen_primes()
x = []
y = 0
while y < 10:
	x += {next(primes_generator)}
	y += 1

print(x)
