#Pat McDonald - 8/2/2018
#Exercise 3: Collatz conjecture
#Week 3 of Programming and Scripting
#Inspired by Reddit!: https://www.reddit.com/r/Python/comments/57r6bf/collatz_conjecture_program/?st=jdhil1j5&sh=ba8fd995

n = int(input("Type an integer: "))
print(n)
while n != 1:
    if (n % 2 == 0):
#(n / 2) outputs a float , so I tried //
        n = n // 2 
        print(n)
    else:
        n = (3 * n) + 1
        print(n)
