"""Find palindromes (letter palingrams) in a dictionary file."""
import load_dictionary


def main():
    word_list = load_dictionary.load('2of4brif.txt')
    pali_list = []

    for word in word_list:
        if len(word) > 1 and word == word[::-1]:
            pali_list.append(word)

    print("\nNumber of palindromes found =", len(pali_list))
    print(*pali_list, sep='\n')

main()
