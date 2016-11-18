'''
Write a Python program that accept an integer (n) and computes the value of n+nn+nnn.
Sample value of n is 5
Expected Result : 615
'''

number = raw_input("Enter the number: ")
print int(number) + int(number*2) + int(number*3)