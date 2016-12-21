'''
Write a Python program to check whether a string starts with specified characters.
'''

inp = raw_input("Enter the string: ")
chr = raw_input("Enter the characters: ")

if inp.lstrip().lower().startswith(chr.rstrip().lower()):
    print "String", inp, 'starts with', chr
else:
    print "String", inp, 'does not starts with', chr