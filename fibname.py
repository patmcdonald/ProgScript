# Pat McDonald
# Exercise 2, Week 2 of Programming and Scripting
# Original code by Ian McLoughlin
# A program that displays Fibonacci numbers using people's names.
# This script includes the python ord() function 
'''My surname is McDonald

The first letter M is number 77

The last letter d is number 100

Fibonacci number 177 is 4378519841510949178490918731459856482

ord() is a built-in function of python 3.6

From https://docs.python.org/3/library/functions.html#ord :

"Given a string representing one Unicode character, return an integer representing the Unicode code point of that character. For example, ord('a') returns the integer 97 and ord('€') (Euro sign) returns 8364. This is the inverse of chr()."'''


def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

name = "McDonald"
first = name[0]
last = name[-1]
firstno = ord(first)
lastno = ord(last)
x = firstno + lastno

ans = fib(x)
print("My surname is", name)
print("The first letter", first, "is number", firstno)
print("The last letter", last, "is number", lastno)
print("Fibonacci number", x, "is", ans)
