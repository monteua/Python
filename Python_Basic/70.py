'''
Write a Python program to access and print a URL's content to the console
'''

import urllib

url = urllib.urlopen('https://www.google.com.ua/')
print url.read()