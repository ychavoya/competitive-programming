# A. Vanya and Fence
# https://codeforces.com/contest/677/problem/A


def read_ints():
    return [int(num) for num in input().split(" ")]


[_, h] = read_ints()
a = read_ints()

w = 0
for p in a:
    w += 2 if p > h else 1

print(w)
