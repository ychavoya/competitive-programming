# A. Police Recruits
# https://codeforces.com/contest/427/problem/A


def read_ints():
    return [int(num) for num in input().split(" ")]


input()
events = read_ints()

untreated = 0
recruits = 0

for event in events:
    if event == -1:
        if recruits == 0:
            untreated += 1
        else:
            recruits -= 1
    else:
        recruits += event

print(untreated)
