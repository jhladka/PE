#!/usr/bin/python

def is_pandigital(M) :
	if sorted(M) == P : pandigital.append(M)

P = [str(i) for i in range(1,10)]
pandigital = []

for N in range(1,10000):
	m = ''
	integer = 1
	while len(m)<9 : 
		prod = str(N*integer)
		m = m+prod
		integer += 1
	if len(m) == 9 :
		is_pandigital(m)

print max(pandigital)
