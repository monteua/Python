'''
Write a Python program to combine each line from first file with the corresponding line in second file.
'''

with open('file2.txt', 'r') as f1, open('file3.txt', 'r') as f2, open('file4.txt', 'w') as f3:
    f3.truncate()
    for line1, line2 in zip(f1, f2):
        line1 = line1.rstrip()
        f3.write(line1+' '+line2)
