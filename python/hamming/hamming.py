def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("The sequence is not of equal length")
    result = 0
    for dna_strand_a , dna_strand_b in zip(strand_a , strand_b):
        if dna_strand_a != dna_strand_b:
            result += 1
    return result    
