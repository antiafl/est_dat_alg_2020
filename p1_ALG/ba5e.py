# -*- coding: utf-8 -*-
"""
Práctica 1 de  Estructuras de Datos y Algoritmias para
Secuencias Biológicas

BA5E - Find a Highest-Scoring Alignment of Two Strings
"""

import argparse
from Bio import pairwise2 as pw2
from Bio.SubsMat import MatrixInfo as matlist

def main(args):
    print('\nBA5E - Find a Highest-Scoring Alignment of Two Strings\n')
    with open(args.seq_file, 'r') as file:
        input_seq = file.read().replace('\n', '')
    with open(args.align_file, 'r') as file:
        input_align = file.read().replace('\n', '')
     
    print('Alignment file: \n',input_align,'\n')
    print('Sequence file: \n',input_seq,'\n')   
    matrix = matlist.blosum62
    alignments = pw2.align.globalds(input_align, input_seq, matrix,-5, -5)
    print(pw2.format_alignment(*alignments[0]))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='P1 Estructuras Datos y Algoritmias')
    parser.add_argument('--seq_file', type=str)
    parser.add_argument('--align_file', type=str)
    args = parser.parse_args()

    main(args)