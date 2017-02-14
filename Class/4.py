'''
Write a Python class to reverse a string word by word.
Input string : 'hello .py'
Expected Output : '.py hello'
'''

class reverseString:
    def start(self, inp):
        return " ".join((reversed(inp.split())))
print (reverseString().start('hello .py'))