#Pat McDonald - Exercise 1
# Original code by Ian McLoughlin
# A program that displays Fibonacci numbers.
# Exercise 1: Programming and Scripting
def fib(n):
  #This function returns the nth Fibonacci number.
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1

  return i

# Test the function with the following value.
# My name is Pat, therefore my A=16 + T=20
x = 16+20
ans = fib(x)
print("Fibonacci number", x, "is", ans)
