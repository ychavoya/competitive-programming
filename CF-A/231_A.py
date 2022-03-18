# A. Team
# https://codeforces.com/contest/231/problem/A


def read_ints():
    return [int(num) for num in input().split(" ")]


n = int(input())

solved = 0
for i in range(n):
    if sum(read_ints()) >= 2:
        solved += 1

print(solved)
