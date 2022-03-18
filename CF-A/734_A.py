# A. Anton and Danik
# https://codeforces.com/contest/734/problem/A

n = int(input())
games = input()

a_wins = 0
d_wins = 0
for game in games:
    if game == "A":
        a_wins += 1
    else:
        d_wins += 1

if a_wins > d_wins:
    print("Anton")
elif a_wins == d_wins:
    print("Friendship")
else:
    print("Danik")
