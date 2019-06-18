"""Find all word-pair palingrams in a dictionary file."""
import load_dictionary


def main():
    word_list = load_dictionary.load('2of4brif.txt')
    find_palingrams(word_list)
    

def find_palingrams(word_list):



main()
