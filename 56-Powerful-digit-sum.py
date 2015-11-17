#!/usr/bin/python

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
