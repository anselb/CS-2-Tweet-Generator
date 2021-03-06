import time


def clean(text_document):
    """
    Removes the new line characters and punctuation that appears at the end of
    each word.
    """
    clean_text_document = text_document.replace('\n', '')
    clean_text_document = clean_text_document.replace(', ', ' ')
    clean_text_document = clean_text_document.replace('.', ' ')
    clean_text_document = clean_text_document.split(' ')

    for word in clean_text_document:
        word = word.lower()
        if word == '':
            clean_text_document.remove(word)

    return clean_text_document


def histogram_dictionary(text_document):
    """
    inputs a text_file name
    returns histogram (each unique word and number of appearances)
    histogram is a dictionary
    """
    transcript = ""
    with open(text_document, 'r') as f:
        transcript = f.read()

    transcript = clean(transcript)

    histo_dict = {}
    for word in transcript:
        if word in histo_dict:
            histo_dict[word] += 1
        else:
            histo_dict[word] = 1

    return(histo_dict)


def histogram_list_list(text_document):
    """
    inputs a text_file name
    returns histogram (each unique word and number of appearances)
    histogram is a list of lists
    list[0] is the key list[1] is the tokens
    """
    transcript = ""
    with open(text_document, 'r') as f:
        transcript = f.read()

    transcript = clean(transcript)
    transcript.sort()

    histo_list = []
    for word in transcript:
        in_list = False
        # for word_list_index in range(len(histo_list) - 1):
        #     if word == histo_list[word_list_index][0]:
        #         histo_list[word_list_index][1] += 1
        #         in_list = True
        #         break
        for entry in histo_list:
            if entry[0] == word:
                entry[1] += 1
                in_list = True
                break

        if not in_list:
            histo_list.append([word, 1])

    return(histo_list)


def histogram_list_tuples(text_document):
    """
    inputs a text_file name
    returns histogram (each unique word and number of appearances)
    histogram is a list of tuples
    tuple[0] is the key tuple[1] is the tokens
    """
    transcript = ""
    with open(text_document, 'r') as f:
        transcript = f.read()

    transcript = clean(transcript)

    histo_list = []
    for word in transcript:
        in_list = False

        for word_tuple_index in range(len(histo_list)):
            if word == histo_list[word_tuple_index][0] and not in_list:
                tuple_num = histo_list[word_tuple_index][1] + 1
                del histo_list[word_tuple_index]
                histo_list.append((word, tuple_num))
                in_list = True

        if not in_list:
            histo_list.append((word, 1))

    return(histo_list)


def histogram_list_counts(text_document):
    """
    inputs a text_file name
    returns histogram (each unique word and number of appearances)
    TODO: complete function
    """
    transcript = ""
    with open(text_document, 'r') as f:
        transcript = f.read()

    transcript = clean(transcript)

    histo_list = []
    for word in transcript:
        in_list = False
        for word_list_index in range(len(histo_list) - 1):
            if word == histo_list[word_list_index][0]:
                tuple_num = histo_list[word_list_index][1] + 1
                del histo_list[word_list_index]
                histo_list.append((word, tuple_num))
                in_list = True
        if not in_list:
            histo_list.append((word, 1))

    return(histo_list)


def unique_words(histogram):
    """
    takes in a dictionary histogram
    returns number of unique words
    """
    return(len(histogram))


def frequency(word, histogram):
    """
    takes in a word and a dictionary histogram
    returns number of times the word appears
    TODO: return error if word is not in dictionary
    """
    return histogram[word]


def save_histo_to_file(file_name, histogram):
    """
    arguments are a file name to save to and a dictionary histogram
    creates a document named file_name
    """
    with open(file_name, 'w') as f:
        for word in histogram:
            f.write(word + ' ' + str(histogram[word]) + '\n')


if __name__ == '__main__':
    # start = time.time()
    # print(histogram_dictionary('elon_transcript.txt'))
    # finish = time.time()
    # print(finish - start)

    start = time.time()
    print(histogram_list_list('elon_transcript.txt'))
    finish = time.time()
    print(finish - start)
    # print(unique_words(histogram_dictionary('fish.txt')))
    # print(frequency('fish', histogram_dictionary('fish.txt')))
    # save_histo_to_file('fish_histo.txt', histogram_dictionary('fish.txt'))
    # print(histogram_list_list('fish.txt'))
    print(histogram_list_tuples('fish.txt'))
    # histogram_list_counts('fish.txt')
