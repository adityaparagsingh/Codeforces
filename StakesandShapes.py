t = int(input())

for _ in range(t):
    r, s, p = map(int, input().split())

    n = r + s + p
    need = (n + 1) // 2

    ans = []

    x = min(r, p, need)
    ans += ['P'] * x
    need -= x

    y = min(s, r, need)
    ans += ['R'] * y
    need -= y

    z = min(p, s, need)
    ans += ['S'] * z
    need -= z

    ans += ['R'] * (n - len(ans))

    print(''.join(ans))