#!/usr/bin/python3

def count_nucleotide(dna, nucleotide):
    count = 0
    for base in dna:
        if base == nucleotide:
            count +=1
    return count

if __name__ == "__main__":
    dna_seq = "AAAATTTGGCTTTTAAATTTTTCCCC"
    nuc = "A"
    result = count_nucleotide(dna_seq, nuc)
    print(result)
