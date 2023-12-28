orders = input()
position = [0, 0]

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

# N = 0, W = 1, S = 2, E = 3
direction = 0

for order in orders:
    if order == "L":
        direction = (direction + 1) % 4
    elif order == "R":
        direction = (direction + 3) % 4
    elif order == "F":
        position[0] += dx[direction]
        position[1] += dy[direction]

print(position[0], position[1])