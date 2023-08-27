list = [2]
a = 3
while len(list) < 10001:
    b = 0
    for i in range (0, len(list) - 1):
        if a % list[i] == 0:
            b += 1
    if b == 0:
        list.append(a)
    a += 2
print(list[-1])
