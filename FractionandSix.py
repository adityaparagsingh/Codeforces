from collections import Counter

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = input().strip()
    b = input().strip()

    if Counter(a) == Counter(b) + Counter("six"):
        print("YES")
    else:
        print("NO")