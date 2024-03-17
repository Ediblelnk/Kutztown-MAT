from random import randint


def find_probable_prime(n) -> int:
    p = 1

    while (pow(2, p-1, p) != 1):
        p = randint(2**(n-1), (2**n)-1)

    return p


print(find_probable_prime(32))
