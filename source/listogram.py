#!python

from __future__ import division, print_function  # Python 2 and 3 compatibility


class Listogram(list):
    """Listogram is a histogram implemented as a subclass of the list type."""

    def __init__(self, word_list=None):
        """Initialize this histogram as a new list and count given words."""
        super(Listogram, self).__init__()  # Initialize this as a new list
        # Add properties to track useful word counts for this histogram
        self.types = 0  # Count of distinct word types in this histogram
        self.tokens = 0  # Total count of all word tokens in this histogram
        # Count words in given list, if any
        if word_list is not None:
            for word in word_list:
                self.add_count(word)

    def add_count(self, word, count=1):
        """Increase frequency count of given word by given count amount."""
        # Increase word frequency by count
        self.tokens += count
        in_list = False

        for word_count_tuple in self:
            if word_count_tuple[0] == word and not in_list:
                tuple_num = word_count_tuple[1] + count
                self.remove(word_count_tuple)
                self.append((word, tuple_num))
                in_list = True

        if not in_list:
            self.append((word, count))
            self.types += 1

    def frequency(self, word):
        """Return frequency count of given word, or 0 if word is not found."""
        # Retrieve word frequency count
        if self.__contains__(word):
            return self[self._index(word)][1]
        else:
            return 0

    def __contains__(self, word):
        """Return boolean indicating if given word is in this histogram."""
        # Check if word is in this histogram
        in_histo = False

        for word_count_tuple in self:
            if word_count_tuple[0] == word:
                in_histo = True
                break

        return in_histo

    def _index(self, target):
        """Return the index of entry containing given target word if found in
        this histogram, or None if target word is not found."""
        # Implement linear search to find index of entry with target word
        index = None

        for word_count_index in range(len(self)):
            if self[word_count_index][0] == target:
                index = word_count_index
                break

        return index


def print_histogram(word_list):
    print('word list: {}'.format(word_list))
    # Create a listogram and display its contents
    histogram = Listogram(word_list)
    print('listogram: {}'.format(histogram))
    print('{} tokens, {} types'.format(histogram.tokens, histogram.types))
    for word in word_list[-2:]:
        freq = histogram.frequency(word)
        print('{!r} occurs {} times'.format(word, freq))
    print()


def main():
    import sys
    arguments = sys.argv[1:]  # Exclude script name in first argument
    if len(arguments) >= 1:
        # Test histogram on given arguments
        print_histogram(arguments)
    else:
        # Test histogram on letters in a word
        word = 'abracadabra'
        print_histogram(list(word))
        # Test histogram on words in a classic book title
        fish_text = 'one fish two fish red fish blue fish'
        print_histogram(fish_text.split())
        # Test histogram on words in a long repetitive sentence
        woodchuck_text = ('how much wood would a wood chuck chuck'
                          ' if a wood chuck could chuck wood')
        print_histogram(woodchuck_text.split())
        # test = Listogram(woodchuck_text.split())
        # print(test._index('would'))

if __name__ == '__main__':
    main()
