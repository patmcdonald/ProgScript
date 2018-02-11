#Pat McDonald - 8/2/2018
#Exercise 3: Collatz conjecture
#Week 3 of Programming and Scripting

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
