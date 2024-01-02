n = int(input())
a = map(int, input().split())

new_a = sorted(a)

result = 0
length = len(new_a)
for index, item in enumerate(new_a):
    result += (item * (length - index))

print(result)