num1 = 0
num2 = 2520
while num1 != 20:
    num1 = 0
    num2 += 2520
    for i in range(1,21):
        if num2 % i == 0:
            num1 += 1
print(num2)
