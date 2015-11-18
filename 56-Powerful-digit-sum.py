#!/usr/bin/python
"""
A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.
Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?
"""

def sum_digits(M):
	s,m = 0,M
	while m: 
		s += m%10
		m = m/10
	return s

MAX = 1
for N in range(1,100):
	M = N
	for i in range(1,100):
		M *= N 
		MAX = max(sum_digits(M),MAX)

print MAX	
