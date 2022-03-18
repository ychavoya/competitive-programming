# A. Word
# https://codeforces.com/contest/59/problem/A

word = input()

lower = 0
for char in word:
    lower += 1 if char.islower() else -1

if lower < 0:
    print(word.upper())
else:
    print(word.lower())
