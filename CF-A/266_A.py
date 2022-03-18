# A. Stones on the Table
# https://codeforces.com/contest/266/problem/A

input()
stones = input()

if len(stones) == 1:
    print(0)
else:
    removed = 0
    for peek in range(1, len(stones)):
        if stones[peek] == stones[peek - 1]:
            removed += 1
    print(removed)
