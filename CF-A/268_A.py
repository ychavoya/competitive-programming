# A. Games
# https://codeforces.com/contest/268/problem/A


def read_ints():
    return [int(num) for num in input().split(" ")]


n = int(input())
teams = [read_ints() for _ in range(n)]

times = 0
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if teams[i][0] == teams[j][1]:
            times += 1

print(times)
