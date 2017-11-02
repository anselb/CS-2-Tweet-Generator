import sys
from random import randint


def create_words_list(filename):
    with open(filename, 'r') as f:
        dict_words = f.readlines()
    return dict_words


def random_sentence(sentence_length, words_list):
    '''
    inputs:
    what is does:
    returns:
    '''
    chosen_words = []
    dict_words = words_list

    for _ in range(input_sentence_len):
        rand_num = randint(0, len(dict_words) - 1)
        chosen_words.append(dict_words[rand_num].replace('\n', ''))

    return(' '.join(chosen_words))


if __name__ == "__main__":
    input_sentence_len = int(sys.argv[1])
    new_word_list = create_words_list('/usr/share/dict/words')
    print(random_sentence(input_sentence_len, new_word_list))
