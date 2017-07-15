from string import ascii_lowercase


def is_pangram(sentence):
    sentence = sentence.lower()
    if all(letter in sentence for letter in ascii_lowercase):
        return True
    return False
