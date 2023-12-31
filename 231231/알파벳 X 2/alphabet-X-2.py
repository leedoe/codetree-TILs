stack = []
count = [0 for _ in range(52)]
al = list(input())

result = 0
for character in al:
    index = ord(character) - 65
    count[index] += 1

    if len(stack) == 0:
        stack.append(character)
        continue

    if character == stack[-1]:
        stack.pop()
        continue

    if count[index] == 2:
        stack.remove(character)
        result += len(stack)
        continue

    stack.append(character)

print(result)