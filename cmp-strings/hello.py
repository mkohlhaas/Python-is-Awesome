#!/usr/bin/env python

seq1 = "atgcttaaaggcattcaatt"
seq2 = "atgcttaaaggaattccatt"

if __name__ == "__main__":
    zip_seqs = zip(seq1, seq2)
    enum_seqs = enumerate(zip_seqs)
    for i, (a, b) in enum_seqs:
        if a != b:
            print(f"index: {i}")

    print([i for i, (a, b) in enumerate(zip(seq1, seq2)) if a != b])
