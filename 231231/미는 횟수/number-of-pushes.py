a = input()
b = input()

def move(a):
    return f'{a[-1]}{a[:-1]}'

count = 0
while True:
    if count == len(a):
        print('-1')
        break

    if a == b:
        print(count)
        break
    a = move(a)
    count += 1