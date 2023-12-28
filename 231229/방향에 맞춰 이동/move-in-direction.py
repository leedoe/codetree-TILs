n = int(input())

dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]


point = [0, 0]
for i in range(n):
    direction, distance = input().split()
    distance = int(distance)
    if direction == 'E':
        point[0] += dx[0] * distance
    elif direction == 'W':
        point[0] += dx[1] * distance
    elif direction == 'S':
        point[1] += dy[2] * distance
    elif direction == 'N':
        point[1] += dy[3] * distance

print(" ".join(map(str, point)))