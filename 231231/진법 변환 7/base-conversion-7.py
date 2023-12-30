m = float(input())
fr = bin(int(m))

temp = []
while True:
    m = m - int(m)
    res = m * 2
    if res > 1:
        temp.append(1)
    else:
        temp.append(0)
    m = res

    if res % 10 == 0 or len(temp) == 4:
        break

print(f'{fr[2:]}.{"".join(map(str, temp))}')