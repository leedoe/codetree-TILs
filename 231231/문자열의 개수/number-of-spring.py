books = []
while True:
    temp = input()
    if temp == '0':
        break
    books.append(temp)

print(len(books))
print('\n'.join(books[::2]))