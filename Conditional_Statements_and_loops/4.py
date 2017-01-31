'''
Write a Python program to construct the following pattern, using a nested for loop.

*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
'''

x = 5

for i in range(x):
    for j in range(i):
        print ("* ", end="")
    print ("")
for i in range(x, 0, -1):
    for j in range(i):
        print("* ", end="")
    print("")