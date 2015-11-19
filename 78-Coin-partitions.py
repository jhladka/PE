#!/usr/bin/python
 
"""
-> using pentagonal numbers and recurrence relation for partition function P(n).

Let p(n) represent the number of different ways in which n coins can be separated into piles. For example, 
five coins can be separated into piles in exactly seven different ways, so p(5)=7.
OOOOO
OOOO   O
OOO   OO
OOO   O   O
OO   OO   O
OO   O   O   O
O   O   O   O   O
Find the least value of n for which p(n) is divisible by one million.
"""

def pentagonal_nb(p) :
	n = len(p)/2 + 1
	p.append(n*(3*n-1)/2)
	p.append(n*(3*n+1)/2)
	return p

n = 1
P = {}
P[0] = 1
P[1] = 1
penta = [1,2]
while not P[n] % pow(10,6) == 0 :
	n += 1
	if penta[-1] < n : 
		penta = pentagonal_nb(penta)
	P[n] = 0
	i = 0
	while n >= penta[i] :
		P[n] += (-1)**(i//2)*P[n-penta[i]]
		i += 1
		if i >= len(penta) : break
	if n%pow(10,3) == 0 : print n, P[n]

print n, P[n]
