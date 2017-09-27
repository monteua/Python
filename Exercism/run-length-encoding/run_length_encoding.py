def decode(data):
    decoded = ""
    count = 0

    while count < len(data):
        numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

        if data[count] in numbers and data[count+1] in numbers:
            num = int(data[count:count+2])
            decoded += (num*data[count+2])
            count += 3
        else:
            if data[count] in numbers:
                num = int(data[count])
                decoded += num*data[count+1]
                count += 2
            else:
                decoded += data[count]
                count += 1
    return decoded


def encode(data):
    new_string = ""
    current_letter = ""
    count = 0
    if len(data) > 0:
        for letter in data:
            if current_letter is None:
                current_letter = letter
                count = 1
            if current_letter == letter:
                count += 1
            else:
                if count > 1:
                    new_string += str(count)
                    new_string += current_letter
                else:
                    new_string += current_letter

                count = 0
                current_letter = letter
                count += 1
    else:
        return ""
    if count > 1:
        new_string += str(count)
        new_string += current_letter
    else:
        new_string += current_letter
    return new_string
