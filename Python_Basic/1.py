'''Write a Python program to print the following string in a specific format (see the output). Go to the editor
Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky.
Twinkle, twinkle, little star, How I wonder what you are" Output :

Twinkle, twinkle, little star,
	How I wonder what you are!
		Up above the world so high,
		Like a diamond in the sky.
Twinkle, twinkle, little star,
	How I wonder what you are
'''

line1 = 'Twinkle, twinkle, little star,'
line2 = 'How I wonder what you are!'
line3 = 'Up above the world so high,'
line4 = 'Like a diamond in the sky.'
line5 = 'Twinkle, twinkle, little star,'
line6 = 'How I wonder what you are'

print line1 + '\n\t' + line2 + '\n\t\t' + line3 + '\n\t\t' + line4 + '\n' + line5 + '\n\t' + line6
