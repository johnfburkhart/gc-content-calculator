"""
A program that tells you the GC content of a
sequence from a FASTA file
"""

import argparse 
import re

def main():
    # Setup argparse to take file
    parser = argparse.ArgumentParser(description='A script that.')
    parser.add_argument('--sequence_file', '-sf', type=str, help='fasta file path')
    args = parser.parse_args()
    sequence = args.sequence_file
    output(sequence)
# Open the text file in read mode
def read_file(path: str) -> str:
    with open(path, 'r') as file:
        # Read the content of the file and store it in a variable
        file_content = file.read()
    return file_content

# extracts the ids in the fasta headers. Expects ">ID_" format.
# TODO: consider changing this to accept different formats
def extract_ids(seq: str) -> list:
    file = read_file(seq)
    id_regex = r'>([^_]+)_'
    ids = re.findall(id_regex, file)
    return ids

# Convert the string to an array of characters
def extract_sequences(seq: str) -> list:
    file = read_file(seq)
    sequence_regex = r'>[^\n]+\n([ACGT\n]+)'
    sequences = re.findall(sequence_regex, file)
    cleaned_sequences = [sequence.replace('\n', '') for sequence in sequences]

    return cleaned_sequences

# Creates dictionary with sequence ids as keys and sequences 
# as values
def sequence_dictionary(seq: str) -> dict:
    ids = extract_ids(seq)
    sequences = extract_sequences(seq)
    seq_dict = {}
    for i in range(len(sequences)):
        seq_dict[ids[i]] = sequences[i]
    return seq_dict 

# Calculates gc percentage of a sequence string
def gc_percentage(seq: str) -> int:
    sequence_length = len(seq)
    gc_count = 0
    for char in seq:
        if char == "G" or char == "C":
            gc_count += 1 
    percent = (gc_count/sequence_length)*100
    return round(percent, 2) 

# Creates dictionary of sequence ids with their corresponding 
# gc percentage
def gc_content(seq:str) -> dict: 
    seq_dict = sequence_dictionary(seq)
    gc_dict = {} 
    for key, value in seq_dict.items():
        id = key
        sequence = value
        gc_percent = gc_percentage(sequence)
        gc_dict[id] = str(gc_percent) + "%"
    return gc_dict  

def output(seq: str) -> None: 
    percentage_dict = gc_content(seq)
    for key, value in percentage_dict.items():
        id = key
        percentage = value
        print("Sequence " + id + " has a GC content of " + percentage)

if __name__ == "__main__":
    main()