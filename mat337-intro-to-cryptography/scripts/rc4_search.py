from itertools import permutations

n = 10

PermutationList = list(permutations(range(0, 10)))
desired = [5, 5, 2, 5, 2, 8]

for s in PermutationList:
    S = list(s)

    history = []

    i = 0
    j = 0

    for _ in range(0, 6):
        i = (i+1) % n
        j = (j+S[i]) % n

        S[i], S[j] = S[j], S[i]

        history.append(S[(S[i]+S[j]) % n])

    if history == desired:
        print("Found it!", s, history)
        break
