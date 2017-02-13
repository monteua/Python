'''
Write a Python class to find a pair of elements (indices of the two numbers) from a given array whose sum equals a
specific target number.
Input: numbers= [10,20,10,40,50,60,70], target=50
Output: 3, 4
'''

class findPair:
    def get_sum(self, array, target):
        for i in range(len(array)):
            if i > 0:
                if sum([int(array[i]), int(array[i-1])]) == int(target):
                    print (str(i)+',', i+1)

array = [10,20,10,40,50,60,70]
findPair().get_sum(array, 110)
