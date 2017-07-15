from string import ascii_lowercase
def is_isogram(word):
    word = word.lower()
    repeats = {}
    for letter in word:
        if letter in ascii_lowercase:
            if letter in repeats:
                return False
            else:
                repeats[letter] = 1
    return True
