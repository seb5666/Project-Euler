from helper.prime import *
from helper.number import *

def issubset(big,small):
	for s in small:
		if s not in big:
			return False
	return True 

def remove(big, small):
	for s in small:
		if s in big:
			big.remove(s)

primes = simplePrimeGen(1000000)
cyclicPrimes = []
count = 0

while (len(primes) != 0):
	print(len(primes))
	prime = primes[0]
	rots = rotations(prime)
	if issubset(primes,rots):
		for r in rots:
			cyclicPrimes.append(r)
		count += len(rots)
		remove(primes, rots)
	else:
		primes.remove(prime)

print(cyclicPrimes)
print(count)
