#!/usr/bin/python

"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

MAX = 1000

for a in xrange(1, (MAX-3)/3+1) :
	for b in xrange(a+1, (MAX-a)/2) :
		c = MAX-a-b
		if a**2 + b**2 == c**2 : 
			
			break 	# break the inner loop
	# if the inner loop wasn't broken :
	else: 
		continue # continue with the next iteration of the outer loop
	break 	# if the inner loop was broken, break the outer

print a, b, c, a*b*c
