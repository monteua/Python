
def hey(string):
    if string is None or string.strip() == "":
        return "Fine. Be that way!"
    elif string.isupper():
        return "Whoa, chill out!"
    elif string.strip()[-1] == "?":
        return "Sure."
    return "Whatever."

