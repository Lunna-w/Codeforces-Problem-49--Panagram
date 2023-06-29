n = int(input())
si = input().lower()
letters = "abcdefghijklmnopqrstuvwxyz"

for letter in letters:
    if letter not in si:
        print("NO")
        break
else:
    print("YES")