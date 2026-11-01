t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    if n == 1:
        print(a[0])
        continue

    total = sum(abs(x) for x in a)
    neg = sum(1 for x in a if x < 0)
    mn = min(abs(x) for x in a)

    if neg % 2 == 1:
        total -= 2 * mn

    print(total)