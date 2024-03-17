x = 0
m = 13

while (True):
    x += 1
    if (2**x) % m == 12:
        break

print(x)
