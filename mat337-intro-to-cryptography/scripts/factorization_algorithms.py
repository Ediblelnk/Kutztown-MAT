from math import ceil, gcd, sqrt


def fermat_factorize(N: int):
    i = 0
    sN = int(ceil(sqrt(N)))
    while (sN-i > 0):
        x = sN + i
        y = sqrt(x**2 - N)
        if (y == round(y)):
            return (int(x-y), int(x+y))
        i += 1


def pollard_factorize(N: int,):
    for B in range(2, ceil(sqrt(N))):
        a = 2
        for j in range(2, B):
            a = a**j % N
        p = gcd(a-1, N)
        if p != 1 and p != N:
            return (p, int(N/p))
    return "No result"


print(fermat_factorize(22_610_009))
# output: (4751, 4759)
print(pollard_factorize(211_763))
# output: (421, 503)
