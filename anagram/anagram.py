__author__ = 'danlmarmot'

from itertools import permutations
import collections

INPUT_WORD = "deposit"
MIN_ANAGRAM_LEN = 4
WORD_DICT_FILEPATH = '/usr/share/dict/words'


def main():
    words_as_dict = make_word_dict(WORD_DICT_FILEPATH)
    anagrams = look_for_anagrams(INPUT_WORD, words_as_dict)
    save_anagrams(INPUT_WORD, anagrams)
    print_anagrams(INPUT_WORD, anagrams)


def make_word_dict(word_filepath):
    """
    Makes a dictionary of words from a file with one word per line.  Words do not have to be unique.
    :param word_filepath: Filepath to the list of words, such as '/usr/share/dict/words'
    :return: dictionary of words, with key=word and value=number of words counting
    """
    word_dict = collections.defaultdict(lambda: 0)

    for w in open(word_filepath):
        # strip off the /n character with w.strip()
        word_dict[w.lower().strip()] += 1

    return word_dict


def look_for_anagrams(input_word, word_dict, word_length=4):
    """
    Produces anagrams for a given word.  Optionally uses minimum length.
    :param input_word: Input word.
    :param word_dict:
    :param min_length:
    :return:
    """
    anagrams = list()

    for i in range(word_length, len(input_word) + 1):
        # reset this for each string length
        answers_for_strlen = ([])

        for item in permutations(input_word, i):
            test_word = ''.join(item)

            if test_word in word_dict.keys():
                if test_word not in answers_for_strlen and test_word != input_word:
                    answers_for_strlen.append(test_word)

        anagrams += list(answers_for_strlen)

    return anagrams


def save_anagrams(input_word, anagrams):
    # Build report
    r = open("results_for" + input_word + ".txt", "w")
    r.write(anagram_report(input_word, anagrams))
    r.close()

    return


def print_anagrams(input_word, anagrams):
    print anagram_report(input_word, anagrams)

    return


def anagram_report(input_word, anagrams):
    report_header = "Anagrams for " + input_word + ":\n"
    report_summary = "Total number of anagrams found for '" + input_word + "': " + str(len(anagrams)) + "\n"
    report_body = "\n".join(anagrams)
    report = report_header + report_summary + report_body

    return report


if __name__ == '__main__':
    main()
