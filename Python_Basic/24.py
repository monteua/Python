'''
Write a Python program to test whether a passed letter is a vowel or not.
'''

def test_string(s):
    if s in ['a', 'e', 'i', 'o', 'u']:
        print s, 'is vowel.'
    else:
        print s, 'is not vowel.'


if __name__ == '__main__':
    test_string(raw_input("Enter any letter: "))