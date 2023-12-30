n = int(input())
result = 2000
for i in range(n // 5 + 1):
    rest = n - (i * 5)
    div = rest / 3
    if rest // 3 == div:
        if result > i * div:
            result = int(i + div)
if result == 2000:
    print(-1)
else:
    print(result)