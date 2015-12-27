#!/usr/bin/python
from math import sqrt

"""
Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.
If we list the set of reduced proper fractions for d <= 8 in ascending order of size, we get:
1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
It can be seen that there are 3 fractions between 1/3 and 1/2.
How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d <= 12,000?
"""

def primes_less_than(m):
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

def prime_factorization(a) :
	f = []
	for i in Primes :
		if i > a : break
		if a%i == 0 : f.append(i)
	return f

def are_coprime(a,b) :
	m = min(a,b)
	n = max(a,b)
	f = prime_factorization(m)
	for i in f :
		if n%i == 0 : return False
	return True

MAX = 12000
Primes = primes_less_than(MAX+1)
print Primes
N = 0 		# for d=3
for i in xrange(4, MAX+1) :
	for j in xrange(i/3+1,i/2+1) :
		if are_coprime(i,j) == True : 
			N += 1
	print "d =", i," N =",N


