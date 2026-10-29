#!/usr/bin/python3



def is_valid_dna(dna):
    if not dna:
        return False

    valid_bases = {"A", "T", "C", "G"}
    return all(base in valid_bases for base in dna.upper())



def hamming_distance(s1, s2):
    if not is_valid_dna(s1) or not is_valid_dna(s2):
        return None
    if len(s1) != len(s2):
        return None
    return sum(a != b for a, b in zip(s1.upper(), s2.upper()))



if __name__ == "__main__":
    print(f"ATGC vs ATGC: {hamming_distance('ATGC', 'ATGC')}")

