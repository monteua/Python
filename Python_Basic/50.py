'''
Write a Python program to convert the distance (in feet) to inches, yards and miles.
'''

def convertDistance(f):
    print f, 'feet is:'
    print f * 12, 'inches;\nor'
    print f * 0.33, 'yards;\nor'
    print f * 0.00018939375, 'miles.'


if __name__ == '__main__':
    user_input = int(raw_input("Enter the distance in feet: "))
    convertDistance(user_input)