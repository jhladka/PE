#!/usr/bin/python
from math import sqrt

"""
Euler's Totient function, phi(n) [sometimes called the phi function], is used to determine the number of positive numbers less than or equal to n 
which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, phi(9)=6.
The number 1 is considered to be relatively prime to every positive number, so phi(1)=1.
Interestingly, phi(87109)=79180, and it can be seen that 87109 is a permutation of 79180.
Find the value of n, 1 < n < 10^7, for which phi(n) is a permutation of n and the ratio n/phi(n) produces a minimum.
"""

MAX = pow(10,7)

def Primes_less_than(m):
    	P = [2,3,5,7,11,13]
	if m < 17 : return [x for x in P if x < m]
    	candidates = [x for x in xrange(17,m,2) if x%3 and x%5 and x%7 and x%11 and x%13]
    	candidates.reverse()
    	s = m**0.5
    	while candidates <> [] :
        	i = candidates.pop()
        	P.append(i)
        	if i <= s : candidates = filter(lambda x : x%i , candidates)
        	else : break
    	candidates.reverse()
    	P.extend(candidates)
    	return P

def Prime_factors(MAX,primes) :
	prime_factors = {}
	for i in xrange(1,MAX+1) :
		prime_factors[i] = []
	for p in primes :
		n = p
		while n <= MAX :
			prime_factors[n].append(p)
			n += p
	return prime_factors

def Is_permutation(N,M) :
	n, m = [int(x) for x in list(str(N))], [int(x) for x in list(str(M))]
	n.sort()
	m.sort()
	return n == m

primes = Primes_less_than(MAX+1)
MIN = 3
prime_factors = Prime_factors(MAX,primes)
for n in prime_factors :
	if n <> 1 :
		phi = n
		for p in prime_factors[n] :
			phi *= 1-(1./p)
		if Is_permutation(n,int(phi)) == True :
			q = n/phi
			if q < MIN :
				MIN = q
				Nmin = n
				#print Nmin, phi, MIN
print Nmin, MIN
