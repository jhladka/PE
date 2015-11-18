#!/usr/bin/python
from math import sqrt
from itertools import permutations

"""
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.
Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
"""

def primes_less_than(m) :
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

def is_prime(p,primes) :
	if p < 2 or p % 2 == 0 : 
		return False
	if p == 2 : 
		return True
	m = int(sqrt(p)+1)
	i = 1
	while primes[i] <= m :
		if p%primes[i] == 0 : return False
		i += 1
	return True

MAX = 10**5 	# pre vypocet pola prvocisel
P = primes_less_than(MAX) 
I = len(P)
max_sum = 10**5 	# horny odhad vyslednej sumy
five_primes = []
while max_sum >=10**5 :
	for i in xrange(1,I-4) : 	# od 3, pretoze ak by bola na konci 2, nebolo by to prvocislo
		a = str(P[i])
		for j in xrange(i+1,I-3) :
			if P[i]+P[j]+P[j+1]+P[j+2]+P[j+3] >= max_sum : break
			b = str(P[j])
			print a,b,max_sum
			pairs=[a+b,b+a]
			if all((is_prime(int(x),P) for x in pairs)) :
				for k in xrange(j+1,I-2) :
					if P[i]+P[j]+P[k]+P[k+1]+P[k+2] >= max_sum : break
					c = str(P[k])
					pairs = [a+c,c+a,b+c,c+b]
					if all((is_prime(int(x),P) for x in pairs)) :
						for l in xrange(k+1,I-1) :
							if P[i]+P[j]+P[k]+P[l]+P[l+1] >= max_sum : break
							d = str(P[l])
							pairs = [a+d,d+a,b+d,d+b,c+d,d+c]
							if all((is_prime(int(x),P) for x in pairs)) :
								for m in xrange(l+1,I) :
									e = str(P[m])
									pairs = [a+e,e+a,b+e,e+b,c+e,e+c,d+e,e+d]
									S = sum((P[i],P[j],P[k],P[l],P[m]))
									if S < max_sum :
										if all((is_prime(int(x),P) for x in pairs)) :
											max_sum = S
											five_primes = [P[i],P[j],P[k],P[l],P[m]]
											print 'suma = ', max_sum,', ', five_primes
print max_sum

