from math import sqrt, ceil


def encryption(text):
    columns = ceil(sqrt(len(text)))

    result = ""
    for i in range(columns):
        result += text[i::columns]

        result += " "
    return result

if __name__ == "__main__":
    text = "".join(input().strip().split(" "))
    print(encryption(text))
