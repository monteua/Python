'''
Write a Python program to detect the number of local variables declared in a function
'''
x = 4
def count():
    string = 'Hello'
    num = 5
    print ("Hello2")
y = 5
print (count.__code__.co_nlocals)