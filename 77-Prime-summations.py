#!/usr/bin/python
"""
It is possible to write ten as the sum of primes in exactly five different ways:
7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2
What is the first value which can be written as the sum of primes in over five thousand different ways?
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

MAX = 1000
Primes = primes_less_than(MAX) 

N = 4
W = {}
while 1 :
	if N > Primes[-1] : 
		MAX *= 100
		Primes = primes_less_than(MAX)
	P = []
	i = 0
	while Primes[i] < N :
		P.append(Primes[i])
		i += 1
	W[N] = []
	for p in P : 
		if N-p in P and p >= N-p : W[N].append(p)
		if N-p > 3:
			for m in W[N-p] : 
				if m <= p : W[N].append(p)
	if len(W[N]) > 5000 :
		break
	N += 1
print N-1, len(W[N-1])	
print N, len(W[N])	
