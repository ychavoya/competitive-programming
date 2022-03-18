# A. Beautiful Matrix
# https://codeforces.com/contest/263/problem/A


def read_ints():
    return [int(num) for num in input().split(" ")]


x = -1
y = -1
for i in range(5):
    row = read_ints()
    for j in range(5):
        if row[j] == 1:
            y = j
            x = i
d_x = x - 2 if x > 2 else 2 - x
d_y = y - 2 if y > 2 else 2 - y

print(d_x + d_y)
