n = int(input())
a = map(int, input().split())

new_a = sorted(a)

result = max(new_a)
for index, item in enumerate(new_a):
    if index == len(new_a) - 1:
        break
    result += ((item / 2))

print(f'{result:.01f}')