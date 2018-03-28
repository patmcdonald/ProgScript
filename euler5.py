
#https://stackoverflow.com/questions/8024911/project-euler-5-in-python-how-can-i-optimize-my-solution/8025847#8025847
#List comprehensions are faster than for loops:
'''def get_divs(n):
    divs = [x for x in range(1,20) if n % x == 0]
    return divs'''

'''From: https://gist.github.com/PEZ/47534'''
    #It's the Least Common Multiple; lcm(1,2, ..., 20) 
'''def gcd(a, b):
  while b > 0:
    a, b = b, a % b
  return a

def lcm(a, b):
  return (a * b) / gcd(a, b)

llcm = lcm(11, 12)
for n in range(12, 20):
  llcm = lcm(n, llcm)

print(llcm)'''
#From the same GitHub Gist above:

#Found the following on the Euler Problem 3 forum, by signature lassevk
#It's quite neat!
'''i = 1
for k in (range(1, 21)): 
  if i % k > 0: 
    for j in range(1, 21): 
      if (i*j) % k == 0: 
        i *= j 
        break 

print(i)'''

#From:https://code.mikeyaworski.com/python/project_euler/problem_5

#Takes a few seconds to return: findSmallestMultiple(20)
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20? */

# returns smallest multiple that is evenly divisible by all numbers from 1 - n
# returns -1 if multiple does not exist
def findSmallestMultiple(n):
    for i in range(n, factorial(n) + 1, n):
        if isMultiple(i, n):
            return i
    return -1

# checks every number between 1 and n to see if x is a multiple of every number
# returns True if x is found to be a multiple of every number, and False if x is
# found to not be a multiple of any number
def isMultiple(x, n):
    for i in range(1, n):
        if x % i != 0:
            return False
    return True

# returns the n factorial, or -1 if it does not exist
def factorial(n):
    if n > 1: return n * factorial(n - 1)
    elif n >= 0: return 1
    else: return -1

print (findSmallestMultiple(10)) # 2520
print (findSmallestMultiple(20))

