import string

letters = list(string.ascii_uppercase)

fhand = open("p022_names.txt", 'r')
names = []
for i in fhand.read().split(","):
    names.append(i[1:-1])

names = sorted(names)
final_score = 0

def get_score(name):
    name_pos = [i for i,x in enumerate(names) if x == name][0]+1
    letters_sum = 0

    for letter in name:
        letters_sum += [p for p, x in enumerate(letters) if x == letter][0]+1
    return int(letters_sum*name_pos)

for name in names:
    get_score(name)
    final_score += get_score(name)

print ("Final score:", final_score)
