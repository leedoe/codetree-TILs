temp = input().split()
n = int(temp[0])
A = temp[1]

result = 0
for i in range(n):
    if input() == A:
        result += 1

print(result)