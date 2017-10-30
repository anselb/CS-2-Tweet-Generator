import sys
import random


def rearange_words(input_words):
    '''
    Takes a list of words and prints the words in a random order
    input_words is a list of words
    '''
    new_word_order = []
    for words in range(len(input_words)):
        rand_word_index = random.randint(0, len(input_words) - 1)
        new_word_order.append(input_words[rand_word_index])
        print(input_words[rand_word_index], end=" ")
        del input_words[rand_word_index]

    # Different way of joining words instead of
    # print(' '.join(new_word_order))


if __name__ == "__main__":
    arguments = sys.argv[1:]
    rearange_words(arguments)
