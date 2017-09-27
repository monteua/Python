from string import ascii_lowercase


def encrypt_alpha(shifts):
    alpha = ascii_lowercase
    alpha_map = {}

    for letter in alpha:

        full = shifts / 26
        if full >= 1:
            reminder = shifts % 26
            idx = alpha.index(letter) + reminder
            if idx >= 26:
                idx = idx - 26
            alpha_map[letter] = alpha[idx]
        else:
            idx = alpha.index(letter) + shifts
            if idx >= 26:
                idx = idx - 26
            alpha_map[letter] = alpha[idx]
    return alpha_map


def rotate(string, shifts):
    e_alpha = encrypt_alpha(shifts)
    result = ""

    for letter in string:
        if letter.islower() and letter in e_alpha:
            idx = e_alpha[letter]
            result += idx
        elif letter.isupper() and letter.lower() in e_alpha:
            letter = letter.lower()
            idx = e_alpha[letter]
            result += idx.upper()
        else:
            result += letter
    return result
