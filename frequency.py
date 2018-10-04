"""Analyze the word frequencies in a book downloaded from Project Gutenberg."""

import string


def get_word_list(file_name):
    """Read the specified project Gutenberg book.

    Header comments, punctuation, and whitespace are stripped away. The function
    returns a list of the words used in the book as a list. All words are
    converted to lower case.
    """
    f = open(file_name, 'r')
    lines = f.readlines()
    curr_line = 0
    while lines[curr_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
      curr_line += 1
    lines = lines[curr_line+1:]
    end = lines.index('End of the Project Gutenberg EBook of Heart of Darkness, by Joseph Conrad\n')
    lines = lines[:end]
    word_list = []
    to_strip = string.whitespace+string.punctuation+'-'+'“'+'”'
    for i in lines:
        for word in i.split():
            word = word.strip(to_strip).lower()
            if len(word) > 0:
                word_list.append(word)
    return word_list


def get_top_n_words(word_list, n):
    """Take a list of words as input and return a list of the n most
    frequently-occurring words ordered from most- to least-frequent.

    Parameters
    ----------
    word_list: [str]
        A list of words. These are assumed to all be in lower case, with no
        punctuation.
    n: int
        The number of words to return.

    Returns
    -------
    int
        The n most frequently occurring words ordered from most to least.
    frequently to least frequentlyoccurring
    """
    word_count = dict()
    for i in word_list:
        word_count[i] = word_count.get(i, 0) + 1
    word_count = sorted(word_count, key=word_count.get, reverse=True)
    return word_count[:n]


if __name__ == "__main__":
    print("Running WordFrequency Toolbox")
    print(string.whitespace)


HOD = get_word_list("HeartofDarkness.txt")
print(get_top_n_words(HOD, 100))
