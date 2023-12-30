temp = [[] for _ in range(53)]
al = list(input())
result = 0
for n in range(1, 53):
    if n == 1:
        temp[n] = [al[0]]
    else:
        before_al = al.index(al[n - 1])
        if before_al == n - 1:
            temp[n] = temp[n - 1] + [al[n - 1]]
        else:
            temp[n] = list(set(temp[n - 1]) - set([al[n - 1]]))
            if set(temp[n]) != set(temp[before_al]):
                result += 1
print(result // 2)