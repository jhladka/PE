#!/usr/bin/python
    
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

