"""
A program that tells you the GC content of a
sequence from a FASTA file
"""

import argparse 

def main():

    # Setup argparse to take file
    parser = argparse.ArgumentParser(description='A script that.')
    parser.add_argument('--sequence_file', '-sf', type=str, help='fasta file path')
    args = parser.parse_args()
    sequence = args.sequence_file
    sequence_length = len(extract_sequence(sequence))
    sequence_id = extract_id(sequence)
    gc_total = count_gc(sequence)
    gc_content = round(gc_total/sequence_length, 4)
    print("The GC content of sequence " + sequence_id + " is " + str(gc_content*100) + "%")

# Open the text file in read mode
def read_file(path: str) -> str:
    with open(path, 'r') as file:
        # Read the content of the file and store it in a variable
        file_content = file.read()
    return file_content


# Convert the string to an array of characters
def extract_sequence(seq: str) -> str:
    nucleotides = ['A', 'C', 'G', 'T']
    characters_array = list(read_file(seq))
    sequence_array = []
    for char in characters_array:
        if char in nucleotides:
            sequence_array.append(char) 
    return ''.join(sequence_array) 

def extract_id(seq: str) -> str:
    nucleotides = ['A', 'C', 'G', 'T']
    characters_array = list(read_file(seq))
    id_array = []
    for char in characters_array: 
        if char == '_':
            return ''.join(id_array)  
        if char not in nucleotides and char != '\n':
            id_array.append(char) 
    
    return ''.join(id_array) 

def count_gc(seq: str) -> int:
    sequence = extract_sequence(seq)
    gc_count = 0
    for char in sequence:
        if char == "G" or char == "C":
            gc_count += 1 
    return gc_count

if __name__ == "__main__":
    main()