import sys
import time


def anagram_finder(original_word):
    broken_word = []
    broken_anagram = []
    anagram_words = []
    clean_words = []

    for letter in original_word:
        broken_word.append(letter)
    broken_word.sort()

    with open('/usr/share/dict/words', 'r') as f:
        dict_words = f.readlines()

        for word in dict_words:
            clean_words.append(word.replace('\n', ''))

    for word in clean_words:
        if set(word) == set(original_word) and len(word) == len(original_word):
            anagram_words.append(word)

    for word in anagram_words:
        broken_anagram = []
        for letter in word:
            broken_anagram.append(letter)
        broken_anagram.sort()
        print(broken_word)
        print(broken_anagram)
        if broken_anagram != broken_word:
            anagram_words.remove(word)

    print(anagram_words)


if __name__ == "__main__":
    input_word = sys.argv[1]
    start = time.time()
    anagram_finder(input_word)
    finish = time.time()
    print(finish - start)
    print(['e', 'e', 'i', 'l', 'p', 'r', 's'] == ['e', 'i', 'l', 'p', 'p', 'r', 's'])
