#!/usr/bin/python
 
"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""
    
MAX = 1000

N = [3,5]

M = []
for n in N :
	i = 1
	while i*n < MAX :
		M.append(i*n)
		i += 1
		
#print sorted(list(set(M)))
print sum(set(M))

