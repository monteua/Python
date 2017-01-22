'''
Write a Python program to get a dictionary from an object's fields.
'''

class ObjFields(object):
    def __init__(self):
        self.zero = '0'
        self.one = '1'
        self.two = '2'
        self.three = '3'
    
get_dict = ObjFields()
print (get_dict.__dict__)