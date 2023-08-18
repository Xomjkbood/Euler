sum, fib1, fib2 = 0, 0, 1
while fib1 < 4 * 10 ** 6:
    if (fib1 + fib2) % 2 == 0:
        sum += fib1 + fib2
    fib1, fib2 = fib2, fib1 + fib2
print(sum)
