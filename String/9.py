'''
Write a Python program to remove the nth index character from a nonempty string
'''

def remove_character(inp, num):
    inp1 = inp[:int(num)-1]
    inp2 = inp[int(num):]

    return inp1+inp2

print remove_character(raw_input("Enter the string: "), raw_input("Enter the number of character: "))