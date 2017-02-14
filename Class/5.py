'''
Write a Python class which has two methods get_String and print_String. get_String accept a string from the user
and print_String print the string in upper case.
'''

class strMethods:
    def __int__(self):
        self.string = ""

    def get_String(self):
        self.string = input("Enter the string: ")
        strMethods().print_String(self.string)

    def print_String(self, string):
        print (string.upper())

strMethods().get_String()