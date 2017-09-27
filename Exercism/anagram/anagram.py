def detect_anagrams(string, array):
    return [word for word in array if sorted(string.lower()) == sorted(word.lower()) and word.lower() != string.lower()]
