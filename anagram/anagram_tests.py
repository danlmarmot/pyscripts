
__author__ = 'danlmarmot'

import anagram
import unittest


class AnagramTest(unittest.TestCase):

    def test_cars(self):
        word_dict = anagram.make_word_dict("sample_words.txt")
        anagrams = anagram.look_for_anagrams("cars", word_dict=word_dict)
        self.assertItemsEqual(anagrams, ['arcs', 'scar'])

    def test_wrestle(self):
        word_dict = anagram.make_word_dict("sample_words.txt")
        anagrams = anagram.look_for_anagrams("wrestle", word_dict=word_dict)
        self.assertItemsEqual(anagrams, ['rest', 'lets', 'reel'])

    def test_wrestle_len3(self):
        word_dict = anagram.make_word_dict("sample_words.txt")
        anagrams = anagram.look_for_anagrams("wrestle", word_dict=word_dict, word_length=3)
        self.assertItemsEqual(anagrams, ['rest', 'lets', 'reel', 'eel'])

if __name__ == '__main__':
    unittest.main()
