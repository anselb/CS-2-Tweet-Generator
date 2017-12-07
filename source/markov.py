from dictogram import Dictogram
import sample
from random import randint

'''
splice
go through index in array and pull next word
'''


def markov_dictograms(text_string):
    text_array = text_string.split()
    dictogram_dictionary = {}

    for word_index in range(len(text_array) - 1):
        current_word = text_array[word_index]
        next_word = text_array[word_index + 1]

        if current_word in dictogram_dictionary:
            dictogram_dictionary[current_word].add_count(next_word)
        else:
            dictogram_dictionary[current_word] = Dictogram([next_word])

    return(dictogram_dictionary)


def nth_markov_dictograms(text_string, nth_order):
    text_array = text_string.split()
    dictogram_dictionary = {}

    for word_index in range(len(text_array) - nth_order):
        current_tuple = tuple((text_array[index]) for index in range(word_index, word_index + nth_order))
        next_word = text_array[word_index + nth_order]

        if current_tuple in dictogram_dictionary:
            dictogram_dictionary[current_tuple].add_count(next_word)
        else:
            dictogram_dictionary[current_tuple] = Dictogram([next_word])

    return(dictogram_dictionary)


def markov_sample(dictogram):
    return sample.weighted_dict_sampling(dictogram)


def markov_chain(dictogram_dictionary):
    # start_word = randint
    dictionary_keys = [key for key, value in dictogram_dictionary.items()]
    sentence_array = [dictionary_keys[randint(0, len(dictionary_keys) - 1)]]

    for word_index in range(10):
        word_dictogram = dictogram_dictionary[sentence_array[word_index]]
        next_word = markov_sample(word_dictogram)
        sentence_array.append(next_word)

    return ' '.join(sentence_array)


def nth_markov_chain(dictogram_dictionary):
    # start_word = randint
    dictionary_keys = [key for key, value in dictogram_dictionary.items()]
    sentence_array = list(dictionary_keys[randint(0, len(dictionary_keys) - 1)])

    nth_order = len(sentence_array)

    for word_index in range(10):
        tuple_as_key = tuple((sentence_array[index]) for index in range(word_index, word_index + nth_order))
        if tuple_as_key in dictogram_dictionary:
            word_dictogram = dictogram_dictionary[tuple_as_key]
            next_word = markov_sample(word_dictogram)
            sentence_array.append(next_word)
        else:
            break

    return ' '.join(sentence_array)


if __name__ == "__main__":
    fish_text = 'one fish two fish red fish blue fish'

    # fish_markov_dictionary = markov_dictograms(fish_text)
    # print(markov_chain(fish_markov_dictionary))

    # fish_markov_dictionary = nth_markov_dictograms(fish_text, 2)
    # print(fish_markov_dictionary)
    # print(nth_markov_chain(fish_markov_dictionary))

    with open('../scraper/corpus.txt', 'r') as myfile:
        elon_corpus = myfile.read().replace('\n', '')

    # elon_markov_dict = markov_dictograms(elon_corpus)
    # print(markov_chain(elon_markov_dict))

    elon_markov_dict = nth_markov_dictograms(elon_corpus, 2)
    print(nth_markov_chain(elon_markov_dict))

    # tuple_test = tuple([1, 2, 3])
    # print(len(tuple_test))
