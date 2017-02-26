'''
Write a Python program to count the frequency of words in a file.
'''


file = (open('text.txt', 'r')).read()
file = file.split("\n")

new_file = []
for i in file:
    i = i.split(" ")
    if len(i) >= 1:
        new_file.append(i)

words = {}

for lst in new_file:
    for item in lst:
        if item not in words:
            words[item] = 1
        else:
            words[item] += 1
print (words)