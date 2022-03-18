# A. Bear and Big Brother
# https://codeforces.com/contest/791/problem/A


def read_ints():
    return [int(num) for num in input().split(" ")]


[a, b] = read_ints()

years = 0
while a <= b:
    a *= 3
    b *= 2
    years += 1

print(years)
