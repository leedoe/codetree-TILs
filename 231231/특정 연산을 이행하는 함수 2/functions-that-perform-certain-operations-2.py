import math
a, b, c = map(float, input().split())

if a == max([a, b, c]):
    a = math.ceil(a)
    if b > c:
        b = round(b)
        c = math.floor(c)
    else:
        b = math.floor(b)
        c = round(c)
elif b == max([a, b, c]):
    b = math.ceil(b)
    if a > c:
        a = round(a)
        c = math.floor(c)
    else:
        a = math.floor(a)
        c = round(c)
elif c == max([a, b, c]):
    c = math.ceil(c)
    if a > b:
        a = round(a)
        b = math.floor(b)
    else:
        a = math.floor(a)
        b = round(b)
print(a, b, c)