# A. Gravity Flip
# https://codeforces.com/contest/405/problem/A


def read_ints():
    return [int(num) for num in input().split(" ")]


input()
cols = read_ints()

new_cols = [str(x) for x in sorted(cols)]

print(" ".join(new_cols))
