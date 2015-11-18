#!/usr/bin/python
    
"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

N = 600851475143

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

P = primes_less_than(int(pow(N,0.5))) 

n = -1
while not N % P[n] == 0 : n -= 1
print P[n]
