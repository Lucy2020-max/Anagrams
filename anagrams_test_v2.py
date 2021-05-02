# Given a words.txt file containing a newline-delimited list of dictionary
# words, please implement the Anagrams class so that the get_anagrams() method
# returns all anagrams from words.txt for a given word.
#
# Requirements:
#   - Optimise the code for fast retrieval
#   - Write more tests
#   - Thread safe implementation

"""
Answers to requirements:
Anagrams are determined associating to each word the sorted list of letters (anagrams). 
1. Code is optimized by creating an index (indexes) including the indexes of word that are anagrams of each other. 
2. Five tests added
3. Thread safe implementation achieved creating a local copy of words.txt in self.words. The file words.txt is never modified in the class Anagrams. 
"""

import unittest

class Anagrams:

    def __init__(self):
        self.words = open('words.txt').readlines()
        self.all_letters = list() # includes list of letters for all the anagrammed words
        self.indexes = dict() # includes indexes of anagrammed words
        count = -1 # initialization of counter of anagrams
        for n in range(len(self.words)):
            letters = list(self.words[n]) 
            if '\n' in letters:
                letters.remove('\n')
                letters.sort()
            if letters not in self.all_letters:
                self.all_letters.append(letters)
                count = count + 1
            if self.indexes.get(count) == None:
                self.indexes[count] = list()
            self.indexes[count].append(n)

    def get_anagrams(self, word):
        word_letters = list(word)
        if '\n' in word_letters:
            word_letters.remove('\n')
        word_letters.sort()
        # finds the letters of the word to process
        ind = self.all_letters.index(word_letters)
        word_anagrams = list()
        # searches for the anagrams of word in the indexes list previously created 
        for n in self.indexes[ind]:
            anagram = self.words[n]
            # removes the '\n' from the anagrams
            if '\n' in anagram:
                anagram = anagram.replace('\n','')
            word_anagrams.append(anagram)
        return word_anagrams


class TestAnagrams(unittest.TestCase):

    def test_anagrams(self):
        anagrams = Anagrams()
        self.assertEqual(anagrams.get_anagrams('plates'), ['palest', 'pastel', 'petals', 'plates', 'pleats', 'staple'])
        self.assertEqual(anagrams.get_anagrams('eat'), ['ate', 'eat', 'eta', 'tea'])
        self.assertEqual(anagrams.get_anagrams('rated'), ['dater', 'rated', 'trade', 'tread'])
        self.assertEqual(anagrams.get_anagrams('diaper'), ['diaper', 'paired', 'repaid'])
        self.assertEqual(anagrams.get_anagrams('esprits'), ['esprits', 'persist', 'spriest', 'sprites', 'stripes'])
        self.assertEqual(anagrams.get_anagrams('parties'), ['parties', 'pastier', 'pirates', 'traipse'])
        self.assertEqual(anagrams.get_anagrams('retrain'), ['retrain', 'terrain', 'trainer'])

if __name__ == '__main__':
    unittest.main()
