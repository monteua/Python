'''
Write a Python program to find three numbers from an array such that the sum of three numbers equal to zero.
Input : [-1,0,1,2,-1,-4]
Output : [[-1, -1, 2], [-1, 0, 1]]
Note : Find the unique triplets in the array.
'''

def find_three(lst):
    #lst.sort()
    summ = []
    for i in range(len(lst)):
        for o in range(len(lst)):
            for p in range(len(lst)):
                if lst[i]+lst[o]+lst[p] == 0 and i != o and o != p and i != p:
                    summ.append([lst[i], lst[o], lst[p]])
    for i in summ:
        for p in summ[1:]:
            if p[0] in i and p[1] in i and p[2] in i:
                summ.remove(p)


    return summ

print (find_three([-1,0,1,2,-1,-4]))
