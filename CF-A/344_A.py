# A. Magnets
# https://codeforces.com/contest/344/problem/A

n = int(input())
last_p = input()[0]

groups = 1
for i in range(n - 1):
    p = input()[0]
    if last_p != p:
        groups += 1
        last_p = p

print(groups)
