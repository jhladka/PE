#!/usr/bin/python

"""
Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20x20 grid?
"""

G = 20

N = [3,2,1]
for g in xrange(3,G+1) :
	n = [0]
	S = 0
	for i in xrange(g) :
		s = sum(N[i:])
		n.append(s)
		S += s
	n[0] = sum(n)
	S += n[0]
	N = n[:]
	print g, S
