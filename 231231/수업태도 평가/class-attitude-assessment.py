n = int(input())
names = ["Bessie", "Elsie", "Daisy", "Gertie", "Annabelle", "Maggie", "Henrietta",]
score = [0, 0, 0, 0, 0, 0, 0]

for _ in range(n):
    name, grade = input().split()
    if name[0] == "B":
        score[0] += int(grade)
    elif name[0] == "E":
        score[1] += int(grade)
    elif name[0] == "D":
        score[2] += int(grade)
    elif name[0] == "G":
        score[3] += int(grade)
    elif name[0] == "A":
        score[4] += int(grade)
    elif name[0] == "M":
        score[5] += int(grade)
    elif name[0] == "H":
        score[6] += int(grade)

worst = min(score)
score = [100000 if x == worst else x for x in score]
worse = min(score)
if len([x for x in score if x == worse]) > 1:
    print("Tie")
else:
    print(names[score.index(worse)])