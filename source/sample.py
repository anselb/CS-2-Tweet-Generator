import histogram
import sys
import time
from random import randint


def random_sampling(histo):
    """
    argument: a histogram
    return: a random word from the histogram (each word has same odds)
    """

    num_of_words = len(histo)
    list_of_words = [word for word in histo]
    random_index = randint(0, num_of_words - 1)
    return list_of_words[random_index]


def weighted_dict_sampling(dict_histo):
    """
    argument: a dictionary histogram
    return: a words from the histogram that was sampled by frequency
    (higher occurance = higer probability to be sampled)
    """

    list_of_words = [word for word in dict_histo]

    total_tokens = 0
    for word in list_of_words:
        total_tokens += dict_histo[word]

    random_num = randint(0, total_tokens - 1)

    for word, value in dict_histo.items():
        word_frequency = value

        while word_frequency > 0:
            if random_num > 0:
                random_num -= 1
                word_frequency -= 1
            else:
                return word


def weighted_list_tup_sampling(list_tup_histo):
    # TODO: create function for sampling from a histogram of a list of tuples
    pass


def random_check(word_list):
    """
    argument: a list of words
    return: a histogram
    histogram creation function meant to check if words look like they are correctly sampled
    """

    random_word_histogram = {}
    for word in word_list:
        if word in random_word_histogram:
            random_word_histogram[word] += 1
        else:
            random_word_histogram[word] = 1

    return random_word_histogram


if __name__ == "__main__":
    text_document = sys.argv[1]
    histo = histogram.histogram_dictionary(text_document)

    random_words = [random_sampling(histo) for _ in range(10000)]
    # print(random_check(random_words))

    start = time.time()
    random_freq_words = [weighted_dict_sampling(histo) for _ in range(100000)]
    finish = time.time()
    print(finish - start)

    print(random_check(random_freq_words))

    for _ in range(10):
        print(weighted_dict_sampling(histo))
