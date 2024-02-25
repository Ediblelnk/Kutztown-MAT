S = [0, 3, 1, 4, 6, 7, 8, 5, 2, 9]
n = len(S)

i = 0
j = 0

history = []

for _ in range(0, 6):
    i = (i+1) % n
    j = (j+S[i]) % n

    S[i], S[j] = S[j], S[i]

    history.append(S[(S[i]+S[j]) % n])

print(history)
