#!/usr/bin/python

"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
What is the largest n-digit pandigital prime that exists?
"""

from itertools import permutations
from math import sqrt

def is_prime(N):
	sr = int(sqrt(N))
	for i in range(2,sr+1):
		if N%i == 0 : break
	else: 	prime.append(N)

prime = []
for i in range(10,1,-1):
	N = [str(j) for j in range(1,i)]
	n = ''
	for j in N : n += str(j) 
	P = permutations(n)
	for p in P : 
		s=''
		for j in p: s+=str(j)
		is_prime(int(s))
	if prime <> [] : break
print max(prime)	
