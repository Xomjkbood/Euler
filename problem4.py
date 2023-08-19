pol = []
for a in range(999, 100, -1):
    for b in range(999, 100, -1):
        if str(a * b) == str(a * b)[::-1]:
            pol.append(a * b)
print(max(pol))
