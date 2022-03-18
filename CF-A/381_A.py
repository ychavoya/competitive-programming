# A. Sereja and Dima
# https://codeforces.com/contest/381/problem/A


def read_ints():
    return [int(num) for num in input().split(" ")]


input()
cards = read_ints()

p1 = 0
p2 = 0
is_p1 = True
while len(cards) > 0:
    idx = 0 if cards[0] > cards[-1] else -1
    if is_p1:
        p1 += cards.pop(idx)
    else:
        p2 += cards.pop(idx)
    is_p1 = not is_p1

print(p1, p2)
