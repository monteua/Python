def word_count(phrase):
    word_dict = {}
    for word in phrase.strip().lower().split():
        word_input = ''.join(e for e in word if e.isalnum()).strip()
        if word_input:
            word_dict[word_input] = word_dict.get(word_input, 0) + 1
    return word_dict