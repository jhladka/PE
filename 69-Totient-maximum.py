#!/usr/bin/python
from math import sqrt

"""
Euler's Totient function, phi(n) [sometimes called the phi function], is used to determine the number of numbers less than n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, phi(9)=6.
It can be seen that n=6 produces a maximum n/phi(n) for n<=10.
Find the value of n<=1,000,000 for which n/phi(n) is a maximum.
"""

MAX = pow(10,6)

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
	for i in xrange(2,MAX+1) :
		prime_factors[i] = []
	for p in primes :
		n = p
		while n <= MAX :
			prime_factors[n].append(p)
			n += p
	return prime_factors

Nmax = 2
Qmax= 2
primes = Primes_less_than(MAX+1)
prime_factors = Prime_factors(MAX,primes) 	#pole prvociselnych delitelov daneho cisla
for n in prime_factors :
	phi = n
	for p in prime_factors[n] :
		phi *= 1-(1./p)
	q = n/phi
	if q > Qmax :
		Nmax = n
		Qmax = q
		
print Nmax, Qmax
