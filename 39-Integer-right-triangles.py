#!/usr/bin/python

"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
{20,48,52}, {24,45,51}, {30,40,50}
For which value of p ≤ 1000, is the number of solutions maximised?
"""

from math import sqrt

N = 1000

perimeter = [0 for x in range(1,1001)]
for i in range(1,(N-3)/3):
	for j in range(i+1,(N-i-1)/2):
		k = sqrt(i**2+j**2)
		if int(k) == k and i+j+int(k)<=N : perimeter[i+j+int(k)-1] += 1
m = max(perimeter)
print [i+1 for i,j in enumerate(perimeter) if j == m]
