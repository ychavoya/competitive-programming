# A. Black Square
# https://codeforces.com/contest/431/problem/A


def read_ints():
    return [int(num) for num in input().split(" ")]


[a1, a2, a3, a4] = read_ints()
game = input()

calories = 0
for square in game:
    if square == "1":
        calories += a1
    elif square == "2":
        calories += a2
    elif square == "3":
        calories += a3
    else:
        calories += a4

print(calories)
