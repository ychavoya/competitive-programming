# A. Boy or Girl
# https://codeforces.com/contest/236/problem/A

username = input()

seen = []
for letter in username:
    if letter not in seen:
        seen.append(letter)

print("CHAT WITH HER!" if len(seen) % 2 == 0 else "IGNORE HIM!")
