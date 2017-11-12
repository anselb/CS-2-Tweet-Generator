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


def markov_sample(dictogram):
    return sample.weighted_dict_sampling(dictogram)


def markov_chain(dictogram_dictionary):
    # start_word = randint
    sentence_array = ['one']
    for word_index in range(10):
        next_word = markov_sample(dictogram_dictionary[sentence_array[word_index]])
        sentence_array.append(next_word)

    return ' '.join(sentence_array)


if __name__ == "__main__":
    fish_text = 'one fish two fish red fish blue fish'
    fish_markov_dictionary = markov_dictograms(fish_text)
    print(markov_chain(fish_markov_dictionary))
