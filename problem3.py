num = 600851475143
list = []
i = 2
while i < num + 1:
    if num % i == 0:
        list.append(i)
    while num % i == 0:
        num //= i
    i += 1
if num != 1:
    list.append(i)
print(max(list))
