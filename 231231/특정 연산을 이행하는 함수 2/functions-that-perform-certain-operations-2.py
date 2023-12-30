import math
num = list(map(float, input().split()))

a = max(num)
num.remove(a)

a = math.ceil(a)

b = min(num)
num.remove(b)

b = math.floor(b)
c = round(num[0])

print(a, b, c)