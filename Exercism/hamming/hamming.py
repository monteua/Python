def distance(dna, rna):
    result = 0
    if len(dna) == len(rna):
        for i in range(len(dna)):
            if dna[i] != rna[i]:
                result += 1
        return result
    else:
        raise ValueError