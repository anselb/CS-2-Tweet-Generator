import sys
import time
import random


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
            print(word)
            anagram_words.remove(word)

    print(anagram_words)


def fake_anagram(word):
    anagram_letters = [letter for letter in word]

    fake_word = ""
    for letter in range(len(anagram_letters)):
        random_index = random.randint(0, len(anagram_letters) - 1)
        fake_word += anagram_letters[random_index]
        del anagram_letters[random_index]

    print(fake_word)


if __name__ == "__main__":
    input_word = sys.argv[1]

    # start = time.time()
    # anagram_finder(input_word)
    # finish = time.time()
    # print(finish - start)
    # print(['e', 'e', 'i', 'l', 'p', 'r', 's'] == ['e', 'i', 'l', 'p', 'p', 'r', 's'])

    fake_anagram(input_word)
