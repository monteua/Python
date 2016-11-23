'''
Write a Python program to get a new string from a given string where "Is" has been added to the front.
If the given string already begins with "Is" then return the string unchanged.
- See more at: http://www.w3resource.com/python-exercises/python-basic-exercises.php#sthash.Myfv5UHr.dpuf
'''

user_input = raw_input("Enter the string: ")
if user_input.lower().startswith('is'):
    print user_input
else:
    print "Is" + user_input