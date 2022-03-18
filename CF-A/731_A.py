# A. Night at the Museum
# https://codeforces.com/contest/731/problem/A

name = input()

letters = "abcdefghijklmnopqrstuvwxyz"
ptr = 0

total_rotations = 0
for char in name:
    rot = 0
    while rot < 14:
        n_ptr = (ptr + rot) % 26
        if letters[n_ptr] == char:
            total_rotations += rot
            ptr = n_ptr
            break
        rot += 1
    if letters[ptr] == char:
        continue
    rot = 0
    while rot < 14:
        n_ptr = ptr - rot if ptr - rot >= 0 else 26 + ptr - rot
        if letters[n_ptr] == char:
            total_rotations += rot
            ptr = n_ptr
            break
        rot += 1

print(total_rotations)
