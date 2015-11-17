#!/usr/bin/python

"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

def is_palindrome(n) :
	s = str(n)
	if s == s[::-1] : return True
	return False
MAX = 1
for a in range(999,99,-1) :
	for b in range(999,99,-1) :
		if is_palindrome(a*b) == True :
			MAX = max(MAX,a*b) 

print MAX
			
