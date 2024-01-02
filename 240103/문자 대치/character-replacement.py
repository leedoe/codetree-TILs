word = input()
word = word.replace("XXXX", "aaaa")
word = word.replace("XX", "bb")
if "X" in word:
    print("-1")
else:
    print(word)