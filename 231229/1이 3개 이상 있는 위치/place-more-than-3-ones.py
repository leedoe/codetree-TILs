n = int(input())
table = []

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
result = 0

def check(x, y):
    global result
    count = 0
    for i in range(4):
        newx = x + dx[i]
        newy = y + dy[i]

        if newx < 0 or newx >= n:
            continue

        if newy < 0 or newy >= n:
            continue
        
        if table[newy][newx] == 1:
            count += 1

    if count >= 3:
        result += 1

for i in range(n):
    table.append(list(map(int, input().split())))

for y in range(n):
    for x in range(n):
        check(x, y)

print(result)