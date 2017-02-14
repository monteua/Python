'''
Write a Python class to find the three elements that sum to zero from a set of n real numbers.
Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
Output : [[-10, 2, 8], [-7, -3, 10]]
'''

class getThree:
    def get_zero(self, array):

        arrays = []

        for num in array:
            for num2 in array:
                for num3 in array:
                    if num + num2 + num3 == 0:
                        arrays.append([num, num2, num3])
                        array.remove(num)
                        array.remove(num2)
                        array.remove(num3)
        return arrays
array = [-25, -10, -7, -3, 2, 4, 8, 10]
print (getThree().get_zero(array))