def clean(text_document):
    """
    Removes the new line characters and punctuation that appears at the end of
    each word.
    """
    clean_text_document = text_document.replace('\n', '')
    clean_text_document = clean_text_document.replace(',', ' ')
    clean_text_document = clean_text_document.replace('.', ' ')
    return clean_text_document


def histogram(text_document):
    """
    inputs a text and returns a histogram data structure
    returns histogram (each unique word and number of appearances)
    """
    transcript = ""
    with open(text_document, 'r') as f:
        transcript = f.read()

    transcript = clean(transcript)

    transcript.split()
    print(transcript)



def unique_words():
    """
    """

    pass


def frequency():
    """
    """
    pass


if __name__ == '__main__':
    histogram('elon_transcript.txt')
