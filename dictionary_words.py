import sys
from random import randint


def random_sentence(sentence_length):
    chosen_words = []

    with open('/usr/share/dict/words', 'r') as f:
        dict_words = f.readlines()
        for _ in range(input_sentence_len):
            rand_num = randint(0, len(dict_words) - 1)
            chosen_words.append(dict_words[rand_num].replace('\n', ''))

    print(' '.join(chosen_words))


if __name__ == "__main__":
    input_sentence_len = int(sys.argv[1])
    random_sentence(input_sentence_len)
