from math import sqrt

# returns a list of all primes between 1 and n #
# VERY SLOW
def erastotenesSieve(n):
	notmarked = [x for x in range (2,n)]
	for i in range(2,n):
		if i in notmarked:
			print(i)
			temp = i*i
			while temp <= n:
				print(i , ":  ", temp)
				if temp in notmarked:
					notmarked.remove(temp)
				temp += i
	return notmarked

# returns a list of all primes between 1 and n #
# MUCH FASTER THEN ERASTOTENES
def simplePrimeGen(n):
	primes = [2]
	p = 3
	while(p < n):
		test = True
		for prime in primes:
			if prime > sqrt(p) : break
			if p%prime==0:
				test = False
				break
		if test:
			primes.append(p)
			print(p)
		p += 2
	return primes