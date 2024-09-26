""" A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise. """

import re


def is_palindrome(s: str) -> bool:
	s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
	reverse_string = s[::-1]
	return reverse_string == s
	
s='#hih#@'
print(is_palindrome(s)) 
