num1, num2 = 0, 0
for i in range(1, 101):
    num1 += (i ** 2)
for c in range(1, 101):
    num2 += c
print((num2 ** 2) - num1)
