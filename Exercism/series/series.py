def slices(numbers, length):
    result = []
    if length > len(numbers) or length < 1:
        raise ValueError
    else:
        for i in range(len(numbers) - length+1):
            currentNumbers = numbers[i:i+length]
            tempResult = []
            for dig in currentNumbers:
                tempResult.append(int(dig))
            result.append(tempResult)
    return result


