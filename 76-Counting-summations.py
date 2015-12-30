#!/usr/bin/python

"""
It is possible to write five as a sum in exactly six different ways:
4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1
How many different ways can one hundred be written as a sum of at least two positive integers?
"""
nn = [[],[1]]
N = [0,1]
for n in xrange(3,101) :
	nn.append([1])
	for i in xrange(2,n-1) :
		s = 0
		for j in xrange(0,2*i-n-1) :
			s += nn[i-1][j]
		nn[-1].append(N[i-1]-s+(1-(i-1)/(n/2)))
	nn[-1].append(1)
	N.append(sum(nn[-1]))
	print 'N(',n,') = ', N[-1]
