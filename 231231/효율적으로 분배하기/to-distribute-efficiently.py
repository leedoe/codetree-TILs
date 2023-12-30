result = 2000
def div(num, five, three):
    global result
    if num == 0 and result > five + three:
        result = five + three
        return 1
    
    if num < 0:
        return -1
    
    div(num - 5, five + 1, three)
    div(num - 3, five, three + 1)

div(int(input()), 0, 0)
if result == 2000:
    print(-1)
else:
    print(result)