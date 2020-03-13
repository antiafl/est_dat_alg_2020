# -*- coding: utf-8 -*-
"""
Práctica 1 de  Estructuras de Datos y Algoritmias para
Secuencias Biológicas

BA5G - Compute the Edit Distance Between Two Strings
"""

import argparse
import editdistance

def main(args):
    print('\nBA5G - Compute the Edit Distance Between Two Strings\n')
    with open(args.seq_file, 'r') as file:
        input_seq = file.read().replace('\n', '')
    with open(args.align_file, 'r') as file:
        input_align = file.read().replace('\n', '')
  
    print('Alignment file: \n',input_align,'\n')
    print('Sequence file: \n',input_seq,'\n')
    print('Edit distance: \n',editdistance.eval(input_align, input_seq),'\n')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='P1 Estructuras Datos y Algoritmias')
    parser.add_argument('--seq_file', type=str)
    parser.add_argument('--align_file', type=str)
    args = parser.parse_args()

    main(args)