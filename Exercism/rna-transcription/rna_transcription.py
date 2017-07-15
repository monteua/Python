def to_rna(convert):
    dna = ["G", "C", "T", "A"]
    rna = ["C", "G", 'A', "U"]

    result = ""
    for i in range(len(convert)):
        if convert[i] in dna:
            pos = [p for p,x in enumerate(dna) if x == convert[i]]
            result += rna[pos[0]]
    if len(result) == len(convert):
        return result
    else:
        return ""